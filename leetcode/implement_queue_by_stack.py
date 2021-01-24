# -*- coding: utf-8 -*-


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.peek()
    print(param_2)
    param_3 = obj.pop()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
