from pyfakefs.fake_filesystem_unittest import Patcher


patcher = Patcher()
patcher.setUp()

patcher.fs.CreateFile("/foo/bar", contents="demo01")
patcher.fs.CreateFile("/foo/ods", contents="demo02")

with open("/foo/bar", "r") as f:
    data = f.read()
    print data

with open("/foo/ods", "r") as f:
    data = f.read()
    print data

patcher.tearDown()
