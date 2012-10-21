#!/usr/bin/env python
# Copyright 2012 Google Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""VFS Handler which provides access to the raw physical memory.

Memory access is provided by use of a special driver. Note that it is preferred
to use this VFS handler rather than directly access the raw handler since this
handler protects the system from access unmapped memory regions such as DMA
regions. It is always safe to access all of memory using this handler.
"""


import struct
import sys

from grr.client import vfs
from grr.lib import utils
from grr.proto import jobs_pb2


class MemoryVFS(vfs.VFSHandler):
  """A base class for memory drivers."""

  def __init__(self, base_fd, pathspec):
    _ = base_fd
    self.pathspec = pathspec

  @classmethod
  def Open(cls, base_fd, component, pathspec=None):
    _ = pathspec
    return cls(base_fd, pathspec=component)

  def IsDirectory(self):
    return False

  def Stat(self):
    result = jobs_pb2.StatResponse(st_size=self.size)
    result.pathspec.MergeFrom(self.pathspec)
    return result

if "linux" in sys.platform:

  class LinuxMemory(MemoryVFS):
    """A Linux memory VFS driver."""

    supported_pathtype = jobs_pb2.Path.MEMORY
    auto_register = True

    def __init__(self, base_fd, pathspec=None):
      """Open the raw memory image.

      Args:
        base_fd: The file like object we read this component from.
        pathspec: An optional pathspec to open directly.
      Raises:
        IOError: If the file can not be opened.
      """
      super(LinuxMemory, self).__init__(base_fd, pathspec=pathspec)
      if self.base_fd is not None:
        raise IOError("Memory driver must be a top level.")

      # The linux memory acquisition driver is very easy to use.
      self.fd = open(pathspec.path, "rb")
      self.fd.seek(0, 2)
      self.size = self.fd.tell()
      self.fd.seek(0)

    def Read(self, length):
      return self.fd.read(length)

    def Seek(self, offset, whence=0):
      self.fd.seek(offset, whence)

    def Tell(self):
      return self.fd.tell()

# The windows driver has special requirements.
elif sys.platform.startswith("win"):
  # These imports are needed in windows so pylint: disable=C6204
  import win32file

  from grr.client.client_actions.windows import windows

  class WindowsMemory(MemoryVFS):
    """Read the raw memory."""
    supported_pathtype = jobs_pb2.Path.MEMORY
    auto_register = True

    # This is the dtb if available
    cr3 = None

    def __init__(self, base_fd, pathspec=None):
      """Open the raw memory image.

      Args:
        base_fd: The file like object we read this component from.
        pathspec: An optional pathspec to open directly.
      Raises:
        IOError: If the file can not be opened.
      """
      super(WindowsMemory, self).__init__(base_fd, pathspec=pathspec)
      if self.base_fd is not None:
        raise IOError("Memory driver must be a top level.")

      self.pathspec = utils.Pathspec(pathspec)

      # We need to use win32 api to open the device.
      self.fd = win32file.CreateFile(
          pathspec.path,
          win32file.GENERIC_READ | win32file.GENERIC_WRITE,
          win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
          None,
          win32file.OPEN_EXISTING,
          win32file.FILE_ATTRIBUTE_NORMAL,
          None)

      # Obtain the valid memory runs
      data = win32file.DeviceIoControl(
          self.fd, windows.INFO_IOCTRL, "", 1024, None)
      fmt_string = "QQl"
      self.cr3, _, number_of_runs = struct.unpack_from(fmt_string, data)

      offset = struct.calcsize(fmt_string)
      self.runs = []
      self.size = 0
      for x in range(number_of_runs):
        start, length = struct.unpack_from("QQ", data, x * 16 + offset)
        if length == 0: break

        self.runs.append((start, length))
        self.size = start + length

    def Read(self, length):
      """Read from the memory device, null padding the ranges."""
      result = ""
      while length > 0 and self.offset < self.size:
        data = self._PartialRead(length)
        if not data: break

        length -= len(data)
        self.offset += len(data)
        result += data

      return result

    def _PartialRead(self, length):
      last_end = 0
      # Iterate over all the runs and see which one encloses the current file
      # pointer.
      for start, run_length in self.runs:

        # File pointer falls between the last range end and before the current
        # range start (i.e. outside the valid ranges).
        if last_end <= self.offset < start:
          # Zero pad it
          return "\x00" * min(length, start - self.offset)

        last_end = end = start + run_length
        # File pointer falls within a valid range, just read from the device.
        if start <= self.offset < end:
          to_read = min(length, end - self.offset)
          win32file.SetFilePointer(self.fd, self.offset, 0)

          _, data = win32file.ReadFile(self.fd, to_read)

          return data

if "darwin" in sys.platform:
  # The OSX driver needs to perform ioctls to obtain the memory map, so:
  # pylint: disable=C6204
  import array
  import fcntl

  class OSXMemory(MemoryVFS):
    """Read physical memory from pmem driver."""
    # From the drivers pmem_ioctls.h
    pmem_ioc_get_mmap = 0x80087000
    pmem_ioc_get_mmap_size = 0x40047001
    pmem_ioc_get_mmap_desc_size = 0x40047002
    pmem_ioc_get_dtb = 0x40087003
    # (Type, Pad, PhysicalStart, VirtualStart, NumberOfPages, Attribute)
    format_efimemoryrange = "IIQQQQ"
    page_size = 4096
    valid_memory_types = (1,   # Loader Code
                          2,   # Loader Data
                          3,   # BS Code
                          4,   # BS Data
                          5,   # RTS Code
                          6,   # RTS Data
                          7,   # Conventional
                          9,   # ACPI Reclaim
                          10,  # ACPI Memory NVS
                          13,  # Pal Code
                          14)  # Max Memory Type

    supported_pathtype = jobs_pb2.Path.MEMORY
    auto_register = True

    def __init__(self, base_fd, pathspec=None):
      """Open the memory device and get the memory map.

      Args:
        base_fd: The file like object we read this component from.
        pathspec: An optional pathspec to open directly.
      Raises:
        IOError: If the file can not be opened or an ioctl fails.
      """
      super(OSXMemory, self).__init__(base_fd, pathspec=pathspec)
      if self.base_fd is not None:
        raise IOError("Memory driver must be a top level.")

      self.mem_dev = open(pathspec.path, "rb")
      self.mmap = self.GetMemoryMap(self.mem_dev)

    @property
    def size(self):
      start, length = self.mmap[-1]
      return start + length

    @staticmethod
    def GetCR3(mem_dev):
      """Query the memory driver for the kernels CR3 value.

      Args:
        mem_dev: An open file descriptor to the pmem driver.

      Returns:
        The Directory Table Base of the kernels address space
      """
      buf = array.array("L", [0])
      fcntl.ioctl(mem_dev, OSXMemory.pmem_ioc_get_dtb, buf, True)
      return buf[0]

    @staticmethod
    def GetMemoryMap(mem_dev):
      """Obtain and parse the memory map.

      Args:
        mem_dev: An open file descriptor to the pmem driver.

      Returns:
        List of tuples (start_address, number_of_pages)
      """
      size, desc_size = OSXMemory._GetBinaryMemoryMapDimensions(mem_dev)
      mmap = OSXMemory._GetBinaryMemoryMap(mem_dev, size)
      return OSXMemory._ParseBinaryMemoryMap(mmap, size, desc_size)

    @staticmethod
    def _GetBinaryMemoryMapDimensions(mem_dev):
      """Query the memory driver for the memory map dimensions.

      Args:
        mem_dev: An open file descriptor to the pmem driver.

      Returns:
        A Tuple (size, descriptor_size).
      """
      buf = array.array("L", [0])
      fcntl.ioctl(mem_dev, OSXMemory.pmem_ioc_get_mmap_size, buf, True)
      mmap_size = buf[0]
      fcntl.ioctl(mem_dev, OSXMemory.pmem_ioc_get_mmap_desc_size, buf, True)
      mmap_desc_size = buf[0]
      return (mmap_size, mmap_desc_size)

    @staticmethod
    def _GetBinaryMemoryMap(mem_dev, mmap_size):
      """Query the memory driver for the memory map.

      Args:
        mem_dev: An open file descriptor to the pmem driver.
        mmap_size: Size of the memory map in bytes.

      Returns:
        The binary memory map (as an array of EfiMemoryRange structs).
      """
      mmap_buf = array.array("B", " " * mmap_size)
      ptr_mmap_buf = struct.pack("Q", mmap_buf.buffer_info()[0])
      fcntl.ioctl(mem_dev, OSXMemory.pmem_ioc_get_mmap, ptr_mmap_buf)
      return mmap_buf.tostring()

    @staticmethod
    def _ParseBinaryMemoryMap(mmap, size, desc_size):
      """Converts a binary EFI memory map to python tuples of memory segments.

      Args:
        mmap: The binary memory map, an array of EfiMemoryRange structs.
        size: The size in bytes of the memory map.
        desc_size: The size in bytes of an individual EfiMemoryRange struct.

      Returns:
        List of tuples (start_address, number_of_pages)
      """
      num_descriptors = size / desc_size
      result = list()

      for x in xrange(num_descriptors):
        (seg_type, _, start, _, pages, _) = struct.unpack_from(
            OSXMemory.format_efimemoryrange, mmap, x * desc_size)
        if seg_type in OSXMemory.valid_memory_types:
          result.append((start, pages * OSXMemory.page_size))
      return result

    def Read(self, length):
      """Read from the memory device, null padding the ranges."""
      result = ""

      while length > 0 and self.offset < self.size:
        data = self._PartialRead(length)
        if not data: break
        length -= len(data)
        self.offset += len(data)
        result += data
      return result

    def _PartialRead(self, length):
      """Reads from the memory device, stops at segment boundaries."""
      last_end = 0

      # Iterate over all the runs and see which one encloses the current file
      # pointer.
      for section_start, section_length in self.mmap:
        section_end = section_start + section_length
        # File pointer falls between the last range end and before the current
        # range start (i.e. outside the valid ranges).
        if last_end <= self.offset < section_start:
          # Zero pad it
          return "\x00" * min(length, section_start - self.offset)

        last_end = section_end
        # File pointer falls within a valid range, just read from the device.
        if section_start <= self.offset < section_end:
          to_read = min(length, section_end - self.offset)
          self.mem_dev.seek(self.offset)
          return self.mem_dev.read(to_read)
