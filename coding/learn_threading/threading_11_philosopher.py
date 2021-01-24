"""
哲学家就餐问题
五位哲学家围坐在一张桌子前，每个人 面前有一碗饭和一只筷子。
在这里每个哲学家可以看做是一个独立的线程，而每只筷子可以看做是一个锁。
每个哲学家可以处在静坐、 思考、吃饭三种状态中的一个。需要注意的是，每个哲学家吃饭是需要两只筷子的，
这样问题就来了：如果每个哲学家都拿起自己左边的筷子， 那么他们五个都只能拿着一只筷子坐在那儿，直到饿死。
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


def philosopher(left, right):
    # while True:
    with acquire(left, right):
        print(threading.currentThread(), 'eating')


NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

for n in range(NSTICKS):
    t = threading.Thread(target=philosopher, args=(chopsticks[n], chopsticks[(n + 1) % NSTICKS]))
    t.start()
