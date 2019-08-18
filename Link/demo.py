# -*- coding:utf-8 -*-


def insertReverse01(head):
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