# -*- coding:utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value):
        self.stack.append(value)
        self.top += 1
        return value

    def pop(self):
        if self.top == -1:
            print("It is an empty stack")
            return None
        value = self.stack.pop()
        self.top -= 1
        return value

    def get(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def get_size(self):
        return self.top + 1