# -*- coding:utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        self.stack.append(value)
        self.top += 1

    def pop(self):
        if self.is_empty():
            print("The stack is empty")
            return None
        value = self.stack.pop()
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]


class MyQueue:
    def __init__(self):
        self.A = Stack()
        self.B = Stack()

    def push(self, value):
        self.A.push(value)

    def pop(self):
        if self.B.is_empty():
            while not self.A.is_empty():
                self.B.push(self.A.peek())
                self.A.pop()
        value = self.B.pop()
        return value

    def empty(self):
        return self.A.is_empty() and self.B.is_empty()


q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
while not q.empty():
    print(q.pop())