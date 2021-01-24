from mock import patch
import fake_filesystem
import coding.learn_mock.hardware.memory as memory


def fake_fs(path, data):
    fs = fake_filesystem.FakeFilesystem()
    fs.CreateFile(path, contents=data)
    return fake_filesystem.FakeFileOpen(fs)


def demo():

    path = "/proc/meminfo"
    data = """aaa
    bbb
    ccc"""

    path2 = "/proc/vmstat"
    data2 = ""

    with patch.object(memory, "open", fake_fs(path, data)):
        with patch.object(memory.Memory, "func1", return_value=111):
            content1 = memory.data_content1()
            print(content1)
            content2 = memory.Memory.func1()
            print(content2)
