# -*- coding:utf-8 -*-
from DataStructureStackQueue.Queue import Queue


q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
print(q.queue)
print(q.is_empty())
print(q.get_size())
print(q.get_front())
print(q.get_rear())
