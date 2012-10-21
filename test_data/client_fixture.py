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


"""This is a test fixture for client objects.."""


# This file is mostly data so pylint: disable=C6005,C6310


LINUX_FIXTURE = [
    (u"/", ("VFSGRRClient", {
        "metadata:hostname": "Linux%(client_id)s",
        "metadata:system": "Linux",
        "metadata:os_release": "2.6.38.8",
        "metadata:os_version": "#2 SMP Fri Feb 24 03:31:23 PST 2012",
        "metadata:uname": "Linux-#2 SMP Fri Feb 24 03:31:23 PST 2012-2.6.38.8",
        "metadata:clock": "%(age)s329740",
        "metadata:ping": "%(age)s329740",
        "metadata:install_date": "1303680521557627",
        "metadata:ClientInfo": """
client_name: "GRR Monitor"
client_version: 1
revision: 0
build_time: "unknown"
""",
        })),
    ]


# This dict represents a client VFS. It is a list of (path, attributes) tuples,
# where attributes is a tuple of AFF4 object type and a dict of attributes. All
# strings can contain interpolation strings, and protobufs are encoded in text
# form for readability and interpolation-ability.
VFS = [
    (u"/", ("VFSGRRClient", {
        "metadata:hostname": "Host%(client_id)s",
        "metadata:system": "Windows",
        "metadata:os_release": "7",
        "metadata:os_version": "6.1.7600",
        "metadata:uname": "Windows-6.1.7600-7",
        "metadata:clock": "%(age)s329740",
        "metadata:ping": "%(age)s329740",
        "metadata:install_date": "1303680521557627",
        "metadata:ClientInfo": """
client_name: "GRR Monitor"
client_version: 1
revision: 0
build_time: "unknown"
""",
        })),
    # The following deliberately neglects to include proc so we can test if its
    # picked up anyway.
    (u"/fs/os/c/regex.*?][{}--", ("VFSDirectory", {
        })),
    # This is unlinked in other VFSDirectory objects - tests if we correctly
    # merge data store objects.
    (u"/fs/tsk/c/bin", ("VFSDirectory", {
        })),
    (u"/fs/tsk/c/bin/rbash", ("VFSMemoryFile", {
        "aff4:size": 12,
        "aff4:content": "Hello world",
        })),
    (u"/fs/tsk/c/bin/bash", ("VFSMemoryFile", {
        "aff4:size": 12,
        "aff4:content": "Hello world",
        })),
    (u"/fs/os/c/regex\V.*?]xx[{}--", ("VFSDirectory", {
        })),
    (u"/fs/os/c/regex\V.*?]xx[{}--/regexchild", ("VFSDirectory", {
        })),
    (u"/fs/os/proc/", ("VFSDirectory", {
        })),
    (u"/fs/os/c/bin %(client_id)s", ("VFSDirectory", {
        })),
    (u"/fs/os/c/bin %(client_id)s/rbash", ("VFSMemoryFile", {
        "aff4:size": 12,
        "aff4:content": "Hello world",
        })),
    (u"/fs/os/c/bin %(client_id)s/bash", ("VFSMemoryFile", {
        "aff4:size": 12,
        "aff4:content": "Hello world",
        })),
(u"/fs/os/c/bin %(client_id)s/pidof", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1286783
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 18776
st_atime: 1308899687
st_mtime: 1307651432
st_ctime: 1308353809
st_blocks: 40
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/pidof"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/hostname", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026226
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14736
st_atime: 1308955274
st_mtime: 1268260136
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/hostname"
}
"""
})),
(u"/fs/os/c/bin/bash", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026148
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin/bash"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/which", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026179
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 946
st_atime: 1309030669
st_mtime: 1260277502
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/which"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/netstat", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026192
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 120184
st_atime: 1308964271
st_mtime: 1265937325
st_ctime: 1299502221
st_blocks: 248
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/netstat"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mount", ("VFSFile", {
"aff4:stat":
"""
st_mode: 35309
st_ino: 1026189
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 82256
st_atime: 1308964262
st_mtime: 1295553386
st_ctime: 1299502221
st_blocks: 176
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mount"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zmore", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026275
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 2416
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zmore"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ksh93", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026210
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 1322432
st_atime: 1299502220
st_mtime: 1244469385
st_ctime: 1299502221
st_blocks: 2592
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ksh93"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/rnano", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026214
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 191976
st_atime: 1301488817
st_mtime: 1265074241
st_ctime: 1299502221
st_blocks: 384
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/rnano"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/sync", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026204
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 35232
st_atime: 1303294466
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/sync"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mv", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026181
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 97352
st_atime: 1309005675
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 200
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mv"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026258
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39880
st_atime: 1299502220
st_mtime: 1267760625
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mt"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/umount", ("VFSFile", {
"aff4:stat":
"""
st_mode: 35309
st_ino: 1026230
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 56680
st_atime: 1308960934
st_mtime: 1295553386
st_ctime: 1299502221
st_blocks: 120
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/umount"
}
"""
})),
(u"/fs/os/c/中国新闻网新闻中/bzcmp", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026148
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/\344\270\255\345\233\275\346\226\260\351\227\273\347\275\221\346\226\260\351\227\273\344\270\255/bzcmp"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/tailf", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026220
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10552
st_atime: 1299502220
st_mtime: 1295553385
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/tailf"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzless", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026240
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 1297
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzless"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dir", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026250
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 114032
st_atime: 1299502220
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 232
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dir"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/setfont", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026219
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39808
st_atime: 1308269352
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/setfont"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zegrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026183
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zegrep"
}
"""
})),
(u"/fs/os/proc/stat", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
resident: " \\ncpu  114617668 7836954 50675828 1418369363 12839399 70592 632324 0 14217\\ncpu0 29082342 1842609 9317300 355681349 2794715 30088 59242 0 3170\\ncpu1 28922541 2271509 15959609 352451741 3132959 2503 377305 0 3674\\ncpu2 29410623 1856253 9917677 356174053 3732825 23192 117709 0 4343\\ncpu3 27202162 1866583 15481242 354062220 3178900 14809 78068 0 3030\\nctxt 20506983499\\nbtime 1316172528\\nprocesses 66452973\\nprocs_running 2\\nprocs_blocked 0\\n"
pathspec {
  pathtype: OS
  path: "/fs/os/proc/stat"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/uname", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026280
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39360
st_atime: 1309034899
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/uname"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/nisdomainname", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026229
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14736
st_atime: 1299502220
st_mtime: 1268260136
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/nisdomainname"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/sed", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026261
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 69088
st_atime: 1309033744
st_mtime: 1261435126
st_ctime: 1299502221
st_blocks: 144
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/sed"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/egrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026253
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 105688
st_atime: 1308964880
st_mtime: 1267767223
st_ctime: 1299502221
st_blocks: 216
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/egrep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/touch", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026177
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60016
st_atime: 1308928450
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/touch"
}
"""
})),
(u"/fs/os/c/bin/rbash", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026236
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 934336
st_atime: 1309007414
st_mtime: 1271643361
st_ctime: 1299502221
st_blocks: 1840
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin/rbash"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ksh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026210
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 1322432
st_atime: 1299502220
st_mtime: 1244469385
st_ctime: 1299502221
st_blocks: 2592
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ksh"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/uncompress", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026217
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 63
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/uncompress"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/csh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026157
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 150592
st_atime: 1299502220
st_mtime: 1247833437
st_ctime: 1299502221
st_blocks: 304
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/csh"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/true", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026241
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 35216
st_atime: 1308899805
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/true"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzip2recover", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026203
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10392
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzip2recover"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/znew", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026264
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4952
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/znew"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzcat", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026224
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31176
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzcat"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/static-sh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026159
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 1841392
st_atime: 1299502220
st_mtime: 1271966876
st_ctime: 1299502221
st_blocks: 3608
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/static-sh"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zcmp", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026234
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 69
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zcmp"
}
"""
})),
(u"/fs/os", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 106118
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/chgrp", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026265
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64128
st_atime: 1306244872
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 136
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/chgrp"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/pwd", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026167
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39472
st_atime: 1308899801
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/pwd"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/netcat", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026248
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31296
st_atime: 1308964808
st_mtime: 1266733955
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/netcat"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/setupcon", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026169
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10017
st_atime: 1299502220
st_mtime: 1272143857
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/setupcon"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bunzip2", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026162
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31176
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bunzip2"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mail", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1580605
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 97416
st_atime: 1309028378
st_mtime: 1257840311
st_ctime: 1299502309
st_blocks: 200
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mail"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dash", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026266
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 101608
st_atime: 1308966651
st_mtime: 1270164579
st_ctime: 1299502221
st_blocks: 208
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dash"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/domainname", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026239
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14736
st_atime: 1299502220
st_mtime: 1268260136
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/domainname"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/usleep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026218
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 35720
st_atime: 1299502220
st_mtime: 1265928226
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/usleep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/nc.openbsd", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026248
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31296
st_atime: 1308964808
st_mtime: 1266733955
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/nc.openbsd"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ypdomainname", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026209
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14736
st_atime: 1299502220
st_mtime: 1268260136
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ypdomainname"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/less", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026242
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 149496
st_atime: 1309027569
st_mtime: 1257411121
st_ctime: 1299502221
st_blocks: 304
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/less"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ed", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026272
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 48840
st_atime: 1299502220
st_mtime: 1267762314
st_ctime: 1299502221
st_blocks: 96
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ed"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zdiff", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026208
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4424
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zdiff"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/sh.distrib", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026236
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 934336
st_atime: 1309007414
st_mtime: 1271643361
st_ctime: 1299502221
st_blocks: 1840
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/sh.distrib"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 1026118
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/nano", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026214
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 191976
st_atime: 1301488817
st_mtime: 1265074241
st_ctime: 1299502221
st_blocks: 384
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/nano"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/more", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026147
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 35512
st_atime: 1299502220
st_mtime: 1295553385
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/more"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dumpkeys", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026156
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 82184
st_atime: 1299502220
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 176
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dumpkeys"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zsh4", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026199
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 675792
st_atime: 1299502220
st_mtime: 1271643982
st_ctime: 1299502221
st_blocks: 1328
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zsh4"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ntfs-3g", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026171
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 52832
st_atime: 1308269351
st_mtime: 1269527574
st_ctime: 1299502221
st_blocks: 112
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ntfs-3g"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/cat", ("VFSMemoryFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/cat"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dbus-cleanup-sockets", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026301
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10520
st_atime: 1301187151
st_mtime: 1299262962
st_ctime: 1301187156
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dbus-cleanup-sockets"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dmesg", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026149
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10432
st_atime: 1307481506
st_mtime: 1295553385
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dmesg"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dbus-daemon", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026292
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 326784
st_atime: 1309024234
st_mtime: 1299262962
st_ctime: 1301187156
st_blocks: 648
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dbus-daemon"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/chmod", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026273
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60000
st_atime: 1309026817
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/chmod"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dnsdomainname", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026238
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14736
st_atime: 1299502220
st_mtime: 1268260136
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dnsdomainname"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ntfs-3g.secaudit", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026257
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 55848
st_atime: 1299502220
st_mtime: 1269527574
st_ctime: 1299502221
st_blocks: 120
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ntfs-3g.secaudit"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/plymouth", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026227
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 35416
st_atime: 1308269348
st_mtime: 1290547719
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/plymouth"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/kbd_mode", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026231
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10464
st_atime: 1308269352
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/kbd_mode"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzip2", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026166
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31176
st_atime: 1308928443
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzip2"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mountpoint", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026212
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10328
st_atime: 1308353857
st_mtime: 1307651435
st_ctime: 1308353813
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mountpoint"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/fuser", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026178
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31744
st_atime: 1300397154
st_mtime: 1263803640
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/fuser"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/unicode_start", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026243
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 2762
st_atime: 1299502220
st_mtime: 1268404143
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/unicode_start"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dd", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026152
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60120
st_atime: 1307482055
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dd"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/df", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026150
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 76568
st_atime: 1308964288
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 160
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/df"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/lsmod", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026259
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 6152
st_atime: 1299502220
st_mtime: 1271219811
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/lsmod"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/open", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026168
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14752
st_atime: 1299502220
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/open"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ls", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026249
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 114032
st_atime: 1308964882
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 232
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ls"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/grep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026235
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 113912
st_atime: 1309015591
st_mtime: 1267767223
st_ctime: 1299502221
st_blocks: 232
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/grep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/false", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026195
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 35216
st_atime: 1299502220
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/false"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/fgrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026270
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64600
st_atime: 1308353857
st_mtime: 1267767223
st_ctime: 1299502221
st_blocks: 136
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/fgrep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ping6", ("VFSFile", {
"aff4:stat":
"""
st_mode: 35309
st_ino: 1026175
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31448
st_atime: 1299502220
st_mtime: 1268394116
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ping6"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ntfs-3g.usermap", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026281
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14640
st_atime: 1299502220
st_mtime: 1269527574
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ntfs-3g.usermap"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ln", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026245
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 55912
st_atime: 1309027978
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 120
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ln"
}
"""
})),
(u"/fs/os/c/bin", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 1026118
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zforce", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026190
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 2015
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zforce"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/tempfile", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026246
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10376
st_atime: 1306466024
st_mtime: 1260277502
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/tempfile"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/chown", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026206
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64144
st_atime: 1308959430
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 136
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/chown"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/kill", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026173
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 18800
st_atime: 1308917167
st_mtime: 1260992083
st_ctime: 1299502221
st_blocks: 40
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/kill"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/vdir", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026153
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 114032
st_atime: 1299502220
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 232
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/vdir"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/fgconsole", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026155
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10464
st_atime: 1299502220
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/fgconsole"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ps", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026277
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 101232
st_atime: 1308964867
st_mtime: 1260992083
st_ctime: 1299502221
st_blocks: 208
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ps"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/chvt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026176
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10456
st_atime: 1299502220
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/chvt"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/lessfile", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026228
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 6947
st_atime: 1309030099
st_mtime: 1257411119
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/lessfile"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/echo", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026268
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39328
st_atime: 1308964874
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/echo"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ip", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026164
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 226568
st_atime: 1308964271
st_mtime: 1263802269
st_ctime: 1299502221
st_blocks: 456
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ip"
}
"""
})),
(u"/fs/os/proc/10", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
pathspec {
  pathtype: OS
  path: "/fs/os/proc/10"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zcat", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026158
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zcat"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzcmp", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026180
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 2140
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzcmp"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzmore", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026240
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 1297
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzmore"
}
"""
})),
(u"/fs/os/c/中国新闻网新闻中", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 1026118
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/\344\270\255\345\233\275\346\226\260\351\227\273\347\275\221\346\226\260\351\227\273\344\270\255"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/cpio", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026269
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 129320
st_atime: 1308269353
st_mtime: 1267760625
st_ctime: 1299502221
st_blocks: 264
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/cpio"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/stty", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026225
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64048
st_atime: 1308964982
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 136
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/stty"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/loadkeys", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026211
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 111352
st_atime: 1308269352
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 232
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/loadkeys"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ulockmgr_server", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026309
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14712
st_atime: 1299502828
st_mtime: 1297456930
st_ctime: 1299502844
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ulockmgr_server"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zless", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026185
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 1733
st_atime: 1309035816
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zless"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zfgrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026244
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zfgrep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/gzexe", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026223
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 5874
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/gzexe"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/openvt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026168
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 14752
st_atime: 1299502220
st_mtime: 1268404152
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/openvt"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzfgrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026182
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 3642
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzfgrep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/lesskey", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026161
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 15840
st_atime: 1299502220
st_mtime: 1257411121
st_ctime: 1299502221
st_blocks: 32
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/lesskey"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/gzip", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026252
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64168
st_atime: 1309035805
st_mtime: 1282034617
st_ctime: 1299502221
st_blocks: 136
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/gzip"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/busybox", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026159
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 1841392
st_atime: 1299502220
st_mtime: 1271966876
st_ctime: 1299502221
st_blocks: 3608
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/busybox"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mt-gnu", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026258
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39880
st_atime: 1299502220
st_mtime: 1267760625
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mt-gnu"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/nc", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026248
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31296
st_atime: 1308964808
st_mtime: 1266733955
st_ctime: 1299502221
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/nc"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/cp", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026260
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 109648
st_atime: 1308964880
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 224
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/cp"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bsd-csh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026157
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 150592
st_atime: 1299502220
st_mtime: 1247833437
st_ctime: 1299502221
st_blocks: 304
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bsd-csh"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/tcsh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1582543
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 378144
st_atime: 1299502220
st_mtime: 1269299530
st_ctime: 1299502322
st_blocks: 752
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/tcsh"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/lessecho", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026255
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10504
st_atime: 1299502220
st_mtime: 1257411121
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/lessecho"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/lesspipe", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026228
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 6947
st_atime: 1309030099
st_mtime: 1257411119
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/lesspipe"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mkdir", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026184
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 43600
st_atime: 1308964874
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 88
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mkdir"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ping", ("VFSFile", {
"aff4:stat":
"""
st_mode: 35309
st_ino: 1026274
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 35680
st_atime: 1304668794
st_mtime: 1268394116
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ping"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/keyctl", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026191
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 22936
st_atime: 1299502220
st_mtime: 1257410882
st_ctime: 1299502221
st_blocks: 48
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/keyctl"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zsh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026199
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 675792
st_atime: 1299502220
st_mtime: 1271643982
st_ctime: 1299502221
st_blocks: 1328
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zsh"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzdiff", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026180
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 2140
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzdiff"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/rm", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026194
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 64208
st_atime: 1308989582
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 136
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/rm"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/fusermount", ("VFSFile", {
"aff4:stat":
"""
st_mode: 35309
st_ino: 1026308
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 31384
st_atime: 1307404930
st_mtime: 1297456930
st_ctime: 1299502844
st_blocks: 64
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/fusermount"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzegrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026182
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 3642
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzegrep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/readlink", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026278
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 47656
st_atime: 1309027908
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 96
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/readlink"
}
"""
})),
(u"/fs", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 1026248
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mktemp", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026256
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 43600
st_atime: 1308964808
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 88
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mktemp"
}
"""
})),
(u"/fs/os/proc/10/exe", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
symlink: "/bin/ls"
pathspec {
  pathtype: OS
  path: "/fs/os/proc/10/exe"
}
"""
})),
(u"/fs/os/c/proc", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 1026118
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/proc"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/run-parts", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026193
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 19208
st_atime: 1308993422
st_mtime: 1260277502
st_ctime: 1299502221
st_blocks: 40
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/run-parts"
}
"""
})),
(u"/fs/os/proc/10/cmdline", ("VFSMemoryFile", {
"aff4:content": "ls\000hello world\'\000-l",
"aff4:stat":
"""
st_mode: 33261
st_size: 18
resident: "ls\000hello world\'\000-l"
pathspec {
  pathtype: OS
  path: "/fs/os/proc/10/cmdline"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/bzgrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026182
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 3642
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/bzgrep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/rzsh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026199
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 675792
st_atime: 1299502220
st_mtime: 1271643982
st_ctime: 1299502221
st_blocks: 1328
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/rzsh"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/mknod", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026163
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 43488
st_atime: 1299502220
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 88
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/mknod"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/ntfs-3g.probe", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026276
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10432
st_atime: 1299502220
st_mtime: 1269527574
st_ctime: 1299502221
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/ntfs-3g.probe"
}
"""
})),
(u"/fs/os/c", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 10268
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/gunzip", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026197
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 63
st_atime: 1299502220
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 8
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/gunzip"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/rmdir", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026196
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39392
st_atime: 1308899813
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/rmdir"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/login", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026186
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 44992
st_atime: 1299602124
st_mtime: 1297721498
st_ctime: 1299502221
st_blocks: 88
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/login"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/sleep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026279
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 39376
st_atime: 1308980105
st_mtime: 1285093976
st_ctime: 1299502221
st_blocks: 80
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/sleep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/date", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026215
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 68192
st_atime: 1309034900
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 144
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/date"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/sh", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026236
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 934336
st_atime: 1309007414
st_mtime: 1271643361
st_ctime: 1299502221
st_blocks: 1840
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/sh"
}
"""
})),
(u"/fs/os/proc/10/stat", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
resident: "10 (ls) S 0 1 1 0 -1 4202752 31718 3292927869 90 221932 1968 4310 22381445 6056862 20 0 1 0 19 20250624 484 18446744073709551615 1 1 0 0 0 0 0 4096 536962595 18446744073709551615 0 0 0 3 0 0 0 0 8702"
pathspec {
  pathtype: OS
  path: "/fs/os/proc/10/stat"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/su", ("VFSFile", {
"aff4:stat":
"""
st_mode: 35309
st_ino: 1026154
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 36864
st_atime: 1299502220
st_mtime: 1297721498
st_ctime: 1299502221
st_blocks: 72
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/su"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/zgrep", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026262
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 5597
st_atime: 1309035964
st_mtime: 1282034615
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/zgrep"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/tar", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026207
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 344688
st_atime: 1309028185
st_mtime: 1284997756
st_ctime: 1299502221
st_blocks: 688
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/tar"
}
"""
})),
(u"/fs/os/c/bin %(client_id)s/dbus-uuidgen", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026304
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 10424
st_atime: 1303294484
st_mtime: 1299262962
st_ctime: 1301187156
st_blocks: 24
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/bin %(client_id)s/dbus-uuidgen"
}
"""
})),
(u"/fs/os/c/Downloads", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 10268
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads"
}
"""
})),
(u"/fs/os/c/Downloads/a.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/a.txt"
}
"""
})),
(u"/fs/os/c/Downloads/b.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/b.txt"
}
"""
})),
(u"/fs/os/c/Downloads/c.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/c.txt"
}
"""
})),
(u"/fs/os/c/Downloads/d.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/d.txt"
}
"""
})),
(u"/fs/os/c/Downloads/sub1", ("VFSDirectory", {
"aff4:stat":
"""
st_mode: 16877
st_ino: 10268
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 4874
st_atime: 1299502220
st_mtime: 1284154642
st_ctime: 1299502221
st_blocks: 16
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/sub1"
}
"""
})),
(u"/fs/os/c/Downloads/sub1/a.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/sub1/a.txt"
}
"""
})),
(u"/fs/os/c/Downloads/sub1/b.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/sub1/b.txt"
}
"""
})),
(u"/fs/os/c/Downloads/sub1/c.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/sub1/c.txt"
}
"""
})),
(u"/fs/os/c/Downloads/sub1/d.txt", ("VFSFile", {
"aff4:stat":
"""
st_mode: 33261
st_ino: 1026267
st_dev: 51713
st_nlink: 1
st_uid: 0
st_gid: 0
st_size: 60064
st_atime: 1308964274
st_mtime: 1285093975
st_ctime: 1299502221
st_blocks: 128
st_blksize: 4096
st_rdev: 0
pathspec {
  pathtype: OS
  path: "/fs/os/c/Downloads/sub1/d.txt"
}
"""
})),
# The following are registry fixtures for testing registry related stuff.
(u"/registry/HKEY_USERS/S-1-5-21-2911950750-476812067-1487428992-1001/Software/Microsoft/Windows/CurrentVersion/Explorer/ComDlg32/OpenSavePidlMRU/dd/0", ("VFSFile", {
"aff4:stat":
"""
st_mode: 32768
st_size: 148
st_mtime: 1326790084
registry_type: REG_BINARY
pathspec {
  pathtype: REGISTRY
  path: "/HKEY_USERS/S-1-5-21-2911950750-476812067-1487428992-1001/Software/Microsoft/Windows/CurrentVersion/Explorer/ComDlg32/OpenSavePidlMRU/dd/0"
}
registry_data {
  data: "\024\000\037DG\032\003Yr?\247D\211\305U\225\376k0\356~\000t\000\034\000CFSF\026\0002\000\000\340\365\0051@\366E \000test.dd\000\000\000t\032Y^\226\337\323H\215g\0273\274\356(\272\305\315\372\337\237gVA\211G\305\307k\300\266\177<\000\010\000\004\000\357\2761@\306E1@\306E*\000\000\000\226b\001\000\000\0003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\000e\000s\000t\000.\000d\000d\000\000\000B\000\000\000"
}
"""
})),
# This is for testing CollectRunKeys.

(u"/registry/HKEY_USERS/S-1-5-20/Software/Microsoft/Windows/CurrentVersion/Run/Sidebar", ("VFSFile", {
"aff4:stat":
"""
st_mode: 32768
st_size: 51
st_mtime: 1247546054
registry_type: REG_EXPAND_SZ
pathspec {
 path: "/HKEY_USERS/S-1-5-20/Software/Microsoft/Windows/CurrentVersion/Run/Sidebar"
 pathtype: REGISTRY
}
registry_data {
  string: "%%ProgramFiles%%/Windows Sidebar/Sidebar.exe /autoRun"
}
"""
})),
(u"/registry/HKEY_USERS/S-1-5-20/Software/Microsoft/Windows/CurrentVersion/Run/MctAdmin", ("VFSFile", {
"aff4:stat":
"""
st_mode: 32768
st_size: 51
st_mtime: 1247546054
registry_type: REG_EXPAND_SZ
pathspec {
  pathtype: REGISTRY
  path: "/HKEY_USERS/S-1-5-20/Software/Microsoft/Windows/CurrentVersion/Run/Sidebar"
}
registry_data {
  string: "Sidebar.exe"
}
"""
})),
    ]
