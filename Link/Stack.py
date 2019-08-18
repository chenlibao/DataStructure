# -*- coding:utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value):
        self.stack.append(value)
        self.top += 1

    def remove(self):
        if self.top == -1:
            return -1
        else:
            value = self.stack.pop()
            self.top -= 1
            return value

    def get_top_value(self):
        if self.top == -1:
            print("The stack is none")
        else:
            return self.stack[self.top]

    def print_stack(self):
        pass

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
