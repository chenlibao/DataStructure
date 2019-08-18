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
            return None
        value = self.stack.pop()
        self.top -= 1
        return value

    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


def isPopSerial(data1, data2):
    if data1 is None or data2 is None:
        return False
    if len(data1) != len(data2):
        return False
    s = Stack()
    i = 0
    j = 0
    while i < len(data1):
        s.push(data1[i])
        i += 1
        while (not s.is_empty()) and s.get_top() == data2[j]:
            s.pop()
            j += 1
    # 如果是pop序列，则栈为空，且i=j
    return s.is_empty() and i == j


data1 = "12345"
data2 = "32541"
print(isPopSerial(data1, data2))