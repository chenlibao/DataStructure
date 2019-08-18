# coding=utf-8
from DataStructureStackQueue.Stack import Stack


def is_stack_order(source_data, target_data):
    if len(source_data) != len(target_data):
        return False
    i = 0
    j = 0
    s = Stack()
    while i < len(source_data):
        tmp = source_data[i]
        s.push(tmp)
        while not s.is_empty() and s.get() == target_data[j]:
            s.pop()
            j += 1
        i += 1
    if i == j:
        return True
    else:
        return False


data1 = [1,2,3,4,5,6]
data2 = [3,2,1,5,4,6]
print(is_stack_order(data1, data2))