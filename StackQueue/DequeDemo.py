# -*- coding:utf-8 -*-
from collections import deque


d = deque()
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(5)
d.append(5)
d.append(5)
d.append(5)
d.append(5)
d.append(13)
d.append(15)
print(d)
print(d.pop())
print(d)
print(d.popleft())
print(d)
d.appendleft(10)
d.remove(4)
print(d)
print(d.count(5))
d.insert(2, 1)
print("insert:", d)
d.reverse()
print("reverse:", d)
d.rotate(3)
print("rotate: ", d)
print(len(d))