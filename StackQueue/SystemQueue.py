# -*- coding:utf-8 -*-
from collections import deque

"""
设计一个排队系统，比如顾客在公众号上拿号排队等吃饭，
要求每个用户界面上显示：号码id,前边有多少桌等待
如果排队的人入桌吃饭，则相应更新，用户显示的等待数也更新
id是不变的，但等待数wait_num会变
"""


class User:
    def __init__(self, name, id, wait_id):
        self.name = name
        self.id = id
        self.wait_id = wait_id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_wait_id(self):
        return self.wait_id

    def set_name(self, value):
        self.name = value
        return value

    def set_id(self, value):
        self.id = value
        return self.id

    def set_wait_id(self, value):
        self.wait_id = value
        return self.wait_id

class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def push(self, value):
        self.queue.append(value)
        self.rear += 1

    def pop(self):
        if self.front == self.rear:
            print("The queue is empty")
            return None
        value = self.queue.pop()
        self.front += 1
        return value

    def is_empty(self):
        return self.front == self.rear

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            return None
        return self.queue[self.rear-1]


class QueueSystem:
    def __init__(self):
        self.queue = Queue()
        self.size = 0

    def push(self, value):
        self.queue.push(value)
        self.size += 1
        return self.size

    def pop(self):
        value = self.queue.pop()
        self.size -= 1
        return value

    def id(self):
        return self.size + 1

