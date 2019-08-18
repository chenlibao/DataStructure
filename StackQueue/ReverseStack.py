# -*- coding:utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, value):
        self.stack.append(value)
        self.top += 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.stack.pop()
        self.top -= 1
        return value


class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def enQueue(self, value):
        self.queue.append(value)
        self.rear += 1

    def deQueue(self):
        if self.is_empty():
            print("The queue is empty")
            return None
        self.front += 1
        return self.queue[self.front-1]

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            return None
        return self.queue[self.rear-1]


def reverseStack(s):
    q = Queue()
    while not s.is_empty():
        value = s.pop()
        q.enQueue(value)
    while not q.is_empty():
        s.push(q.get_front())
        q.deQueue()
    return s


s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
reverseStack(s)
while not s.is_empty():
    print(s.pop())