# -*- coding:utf-8 -*-
from collections import deque


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_seq(self):
        return self.seq

    def set_seq(self, value):
        self.seq = value

    def equals(self, obj):
        return self.id == obj.get_id()

    def toString(self):
        return "id: " + str(self.id) + ", name: " + self.name + ", seq:" + str(self.seq)


class MyQueue:
    def __init__(self):
        self.q = deque()

    def enQueue(self, u):
        u.set_seq(len(self.q) + 1)
        self.q.append(u)

    def deQueue(self):
        self.q.popleft()
        self.update_seq()

    def update_seq(self):
        i = 1
        for u in self.q:
            u.set_seq(i)
            i = i + 1

    def print_list(self):
        for u in self.q:
            print(u.toString())


if __name__ == "__main__":
    u1 = User(1, "user1")
    u2 = User(2, "user2")
    u3 = User(3, "user3")
    u4 = User(4, "user4")
    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.print_list()
    print("===========dequeue=========")
    queue.deQueue()
    queue.deQueue()
    queue.print_list()