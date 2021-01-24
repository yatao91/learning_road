"""
为程序中的每一个锁分配一个唯一的id
然后只允许按照升序规则来使用多个锁
"""
import threading
from contextlib import contextmanager

_local = threading.local()


@contextmanager
def acquire(*locks):
    # 使用锁对象ID进行排序:id从小到大排序
    locks = sorted(locks, key=lambda x: id(x))

    # 确保不违反先前获取的锁的锁顺序
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError("Lock Order Violation")

    # 获取所有锁
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # 以相反的顺序释放锁
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]
