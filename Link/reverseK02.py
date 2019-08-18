# coding:utf-8
import sys


class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def constructList(num):
    head = LNode(1)
    cur = head
    i = 2
    while i <= num:
        tmp = LNode(i)
        cur.next = tmp
        cur = cur.next
        i += 1
    return head


def print_link(head):
    if head is None or head.next is None:
        return head
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next


def reverse(head):
    if head is None or head.next is None:
        return head
    cur = head.next
    head.next = None
    while cur:
        nex = cur.next
        cur.next = head
        head = cur
        cur = nex
    return head


def reverse2(head):
    if head is None or head.next is None:
        return head
    pre = head
    cur = head.next
    head.next = None
    while cur:
        nex = cur.next
        cur.next = pre

        pre = cur
        cur = nex
    return pre


def reverseK(head, k):
    if head is None or head.next is None or k < 2:
        return head
    pre = head
    begin = head.next
    while begin:
        end = begin
        i = 1
        while i < k:
            if end.next:
                end = end.next
            else:
                return head
            i += 1 # 这个不要遗漏了
        nex = end.next
        end.next = None
        each_head = reverse(begin)
        pre.next = each_head
        begin.next = nex

        pre = begin
        begin = nex
    return head


head1 = constructList(30)
# new_h = reverse(head1)
# new_h = reverse2(head1)
# print_link(new_h)
head_node = LNode(0)
head_node.next = head1
head2 = reverseK(head_node, 7)
cur = head2.next
while cur:
    # print(cur.data,)
    value = str(cur.data) + " "
    sys.stdout.write(value)
    cur = cur.next
