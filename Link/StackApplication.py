# -*- coding:utf-8 -*-
from DataStructure.Stack import Stack
"""
用栈判断一个字符串是否对称，如：abcdcba
"""


def is_symmetry(data):
    s = Stack()
    for char in data:
        s.push(char)
    flag = True
    for char in data:
        value = s.remove()
        if value != char:
            flag = False
    return flag
