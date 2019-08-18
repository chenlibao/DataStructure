# -*- coding:utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value):
        self.stack.append(value)
        self.top += 1

    def pop(self):
        if self.top == -1:
            print("The stack is empty")
            return
        value = self.stack.pop()
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


class MyStack:
    def __init__(self):
        self.stack = Stack()
        self.minStack = Stack()

    def push(self, value):
        self.stack.push(value)
        if self.minStack.is_empty():
            self.minStack.push(value)
        elif value < self.minStack.peek():
            self.minStack.push(value)

    def pop(self):
        if self.stack.is_empty():
            print("The stack is empty")
            return None
        value = self.stack.pop()
        if value == self.minStack.peek():
            self.minStack.pop()
        return value

    def is_empty(self):
        if self.stack.is_empty():
            return True
        else:
            return False

    def mins(self):
        if self.minStack.is_empty():
            return None
        return self.minStack.peek()


s = MyStack()
s.push(6)
s.push(3)
s.push(5)
s.push(2)
s.push(10)
print(s.mins())