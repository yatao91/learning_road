import pyfakefs.fake_filesystem as fake_fs

from mock import patch

fs = fake_fs.FakeFilesystem()
fs.CreateFile("/foo/bar", contents="demo")

with open("/foo/bar", "r") as f:
    data = f.read()
    print data
