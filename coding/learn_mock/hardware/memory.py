

def data_content1():
    with open("/proc/meminfo") as f:
        content = f.readlines()
    return content


def data_content2():
    with open("/proc/vmstat") as f:
        content = f.readlines()
    return content


class Memory:

    @staticmethod
    def func1():
        with open("/proc/vmstat") as f:
            content = f.readlines()
        return content
