#!/usr/bin/env python
# -*- mode: python; encoding: utf-8 -*-

# Copyright 2011 Google Inc.
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

"""OSX specific utils."""


import ctypes
from ctypes import util
import os
import platform


import logging

from grr.client import client_config
from grr.client import client_utils_linux
from grr.lib import utils
from grr.proto import jobs_pb2


def CFStringToPystring(sc, value):
  length = (sc.CFStringGetLength(value) * 4) + 1
  buff = ctypes.create_string_buffer(length)
  # kCFStringEncodingUTF8 = 134217984
  sc.CFStringGetCString(value, buff, length * 4, 134217984)
  return unicode(buff.value, "utf8")


def CFNumToInt32(sc, num):
  tmp = ctypes.c_int32(0)
  result_ptr = ctypes.pointer(tmp)
  # kCFNumberSInt32Type = 3
  sc.CFNumberGetValue(num, 3, result_ptr)
  return result_ptr[0]


def CFDictRetrieve(sc, dictionary, key):
  ptr = ctypes.c_void_p.in_dll(sc, key)
  return sc.CFDictionaryGetValue(dictionary, ptr)


def OSXFindProxies():
  """This reads the OSX system configuration and gets the proxies."""
  sc = ctypes.cdll.LoadLibrary(util.find_library("SystemConfiguration"))

  cftable = [
      ("CFDictionaryGetValue",
       [ctypes.c_void_p, ctypes.c_void_p],
       ctypes.c_void_p),
      ("CFStringGetLength",
       [ctypes.c_void_p],
       ctypes.c_int32),
      ("CFStringGetCString",
       [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int32, ctypes.c_int32],
       ctypes.c_int32),
      ("CFNumberGetValue",
       [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p],
       ctypes.c_int32),
      ("CFRelease",
       [ctypes.c_void_p],
       None),
      ("SCDynamicStoreCopyProxies",
       [ctypes.c_void_p],
       ctypes.c_void_p),
      ]

  # We need to define input / output parameters for all functions we use
  for (func, args, res) in cftable:
    f = getattr(sc, func)
    f.argtypes = args
    f.restype = res

  # Get the dictionary of network proxy settings
  settings = sc.SCDynamicStoreCopyProxies(None)
  if not settings:
    return []

  try:
    cf_http_enabled = CFDictRetrieve(sc, settings,
                                     "kSCPropNetProxiesHTTPEnable")
    if cf_http_enabled and bool(CFNumToInt32(sc, cf_http_enabled)):
      # Proxy settings for HTTP are enabled
      cfproxy = CFDictRetrieve(sc, settings, "kSCPropNetProxiesHTTPProxy")
      cfport = CFDictRetrieve(sc, settings, "kSCPropNetProxiesHTTPPort")
      if cfproxy and cfport:
        proxy = CFStringToPystring(sc, cfproxy)
        port = CFNumToInt32(sc, cfport)
        result = ["http://%s:%d/" % (proxy, port)]
        result.extend(client_config.PROXY_SERVERS)
        return result

    cf_auto_enabled = CFDictRetrieve(sc, settings,
                                     "kSCPropNetProxiesProxyAutoConfigEnable")
    if cf_auto_enabled and bool(CFNumToInt32(sc, cf_auto_enabled)):
      cfurl = CFDictRetrieve(sc, settings,
                             "kSCPropNetProxiesProxyAutoConfigURLString")
      if cfurl:
        unused_url = CFStringToPystring(sc, cfurl)
        # TODO(user): Auto config is enabled, what is the plan here?
        # Basically, all we get is the URL of a javascript file. To get the
        # correct proxy for a given URL, browsers call a Javascript function
        # that returns the correct proxy URL. The question is now, do we really
        # want to start running downloaded js on the client?
        return client_config.PROXY_SERVERS

  finally:
    sc.CFRelease(settings)
  return client_config.PROXY_SERVERS


def GetMountpoints():
  """List all the filesystems mounted on the system."""
  devices = {}

  for filesys in GetFileSystems():
    devices[filesys.f_mntonname] = (filesys.f_mntfromname,
                                    filesys.f_fstypename)

  return devices


class StatFSStruct(utils.Struct):
  """Parse filesystems getfsstat."""
  _fields = [
      ("h", "f_otype;"),
      ("h", "f_oflags;"),
      ("l", "f_bsize;"),
      ("l", "f_iosize;"),
      ("l", "f_blocks;"),
      ("l", "f_bfree;"),
      ("l", "f_bavail;"),
      ("l", "f_files;"),
      ("l", "f_ffree;"),
      ("Q", "f_fsid;"),
      ("l", "f_owner;"),
      ("h", "f_reserved1;"),
      ("h", "f_type;"),
      ("l", "f_flags;"),
      ("2l", "f_reserved2"),
      ("15s", "f_fstypename"),
      ("90s", "f_mntonname"),
      ("90s", "f_mntfromname"),
      ("x", "f_reserved3"),
      ("16x", "f_reserved4")
  ]


class StatFS64Struct(utils.Struct):
  """Parse filesystems getfsstat for 64 bit."""
  _fields = [
      ("<L", "f_bsize"),
      ("l", "f_iosize"),
      ("Q", "f_blocks"),
      ("Q", "f_bfree"),
      ("Q", "f_bavail"),
      ("Q", "f_files"),
      ("Q", "f_ffree"),
      ("l", "f_fsid1"),
      ("l", "f_fsid2"),
      ("l", "f_owner"),
      ("L", "f_type"),
      ("L", "f_flags"),
      ("L", "f_fssubtype"),
      ("16s", "f_fstypename"),
      ("1024s", "f_mntonname"),
      ("1024s", "f_mntfromname"),
      ("32s", "f_reserved")
  ]


def GetFileSystems():
  """Make syscalls to get the mounted filesystems.

  Returns:
    A list of Struct objects.

  Based on the information for getfsstat
  http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man2/getfsstat.2.html
  """
  major, minor = platform.mac_ver()[0].split(".")[0:2]
  libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))

  if major <= 10 and minor <= 5:
    use_64 = False
    fs_struct = StatFSStruct
  else:
    use_64 = True
    fs_struct = StatFS64Struct

  # Get max 20 file systems.
  struct_size = fs_struct.GetSize()
  buf_size = struct_size * 20

  cbuf = ctypes.create_string_buffer(buf_size)

  if use_64:
    # MNT_NOWAIT = 2 - don't ask the filesystems, just return cache.
    ret = libc.getfsstat64(ctypes.byref(cbuf), buf_size, 2)
  else:
    ret = libc.getfsstat(ctypes.byref(cbuf), buf_size, 2)

  if ret == 0:
    logging.debug("getfsstat failed err: %s", ret)
    return []
  return ParseFileSystemsStruct(fs_struct, ret, cbuf)


def ParseFileSystemsStruct(struct_class, fs_count, data):
  """Take the struct type and parse it into a list of structs."""
  results = []
  cstr = lambda x: x.split("\0", 1)[0]
  for count in range(0, fs_count):
    struct_size = struct_class.GetSize()
    s_data = data[count * struct_size:(count + 1) * struct_size]
    s = struct_class(s_data)
    s.f_fstypename = cstr(s.f_fstypename)
    s.f_mntonname = cstr(s.f_mntonname)
    s.f_mntfromname = cstr(s.f_mntfromname)
    results.append(s)
  return results


def OSXSplitPathspec(pathspec):
  """Splits a given path into (device, mountpoint, remaining path).

  Examples:

  Let's say "/dev/disk0s1" is mounted on "/", then

  /mnt/data/directory/file.txt is split into
  (device="/dev/disk0s1", mountpoint="/", path="mnt/data/directory/file.txt")

  and

  /dev/disk0s1/home/test/ is split into ("/dev/disk0s1", "/", "home/test/").

  After the split, mountpoint and path can always be concatenated
  to obtain a valid os file path.

  Args:
    pathspec: Path specification to be split.

  Returns:
    Pathspec split into device, mountpoint, and remaining path.

  Raises:
    IOError: Path was not found on any mounted device.

  """

  # Splitting the pathspec is exactly the same as on Linux, we just
  # have use the OSX GetMountpoints function.

  return client_utils_linux.LinSplitPathspec(pathspec, GetMountpoints)


def OSXGetRawDevice(path):
  """Resolve the raw device that contains the path."""
  device_map = GetMountpoints()

  path = utils.SmartUnicode(path)
  mount_point = path = utils.NormalizePath(path, "/")

  result = jobs_pb2.Path()
  result.pathtype = jobs_pb2.Path.OS

  # Assign the most specific mount point to the result
  while mount_point:
    try:
      result.path, fs_type = device_map[mount_point]
      if fs_type in ["ext2", "ext3", "ext4", "vfat", "ntfs",
                     "Apple_HFS", "hfs", "msdos"]:
        # These are read filesystems
        result.pathtype = jobs_pb2.Path.OS
      else:
        result.pathtype = jobs_pb2.Path.UNKNOWN

      # Drop the mount point
      path = utils.NormalizePath(path[len(mount_point):])

      return result, path
    except KeyError:
      mount_point = os.path.dirname(mount_point)


def CanonicalPathToLocalPath(path):
  """OSX uses a normal path."""
  return path


def LocalPathToCanonicalPath(path):
  """OSX uses a normal path."""
  return path