# -*- coding: utf-8 -*-
from collections import deque


d = deque("abcdef")

print(d)
print(len(d))
print(d[0])
print(d[-1])

# 1.从右侧添加一个元素
d.append('g')
print(d)

# 2.从右侧添加多个元素
d.extend(['h', 'i'])
print(d)

# 3.从左侧添加一个元素
d.appendleft('hardware')
print(d)

# 4.从左侧添加多个元素
d.extendleft(['b', 'b'])
print(d)

# 5.从右端移除元素
elem = d.pop()
print(elem, d)

# 6.从左侧移除元素
elem2 = d.popleft()
print(elem2, d)

# 7.旋转移动元素：
# +n:向右移动n位，将队列右端的n个元素移动到左端
d.rotate(2)
print(d)

# -n:向左移动n位，将队列左端的n个元素移动到右端
d.rotate(-2)
print(d)

# 8.统计队列中某元素个数
a_num = d.count('hardware')
print(d, a_num)

# 9.反转队列
d.reverse()
print(d)

# 10.移除某元素---移除第一个出现的此元素
d.remove('hardware')
print(d)

# 11.设置队列长度，当新元素加入这个队列且队列已满时，最老的元素被自动剔除掉
d1 = deque(maxlen=3)
d1.append(1)
d1.append(2)
d1.append(3)
print(d1)
d1.append(4)
print(d1)
d1.appendleft(5)
print(d1)

d2 = deque(range(10), 4)
print(d2)
