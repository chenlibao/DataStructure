# -*- coding:utf-8 -*-
from DataStructure.LinkedList import LinkedList
"""
: k >= 2
"""


def reverse_k(head, k):
    if head is None or head.next is None:
        return head

    rear = head
    count = 1
    while rear and count < k:
        rear = rear.next
        count += 1
    sub_head = None
    if count == k:
        sub_head = rear.next

    pre = head
    cur = head.next
    while cur:
        nex = cur.next
        cur.next = pre

        new_head = reverse_k(sub_head, k)
        pre.next = new_head

        pre = cur
        cur = nex

    return head


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def constructLink(num):
#     head = Node(0)
#     cur = head
#     for i in range(1, num):
#         node = Node(i)
#         cur.next = node
#         cur = cur.next
#     return head

link = LinkedList()
print("=======before========")
link.add(1)
link.add(2)
link.add(3)
link.add(4)
link.add(5)
link.add(6)
link.add(7)
link.print_list()
print("=======reverse_k(head, 2)========")
newHead = reverse_k(link.head, 2)
c = newHead
while c:
    print(c.data)
    c = c.next

