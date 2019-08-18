# -*- coding:utf-8 -*-
from DataStructure.LinkedList01 import LinkedList01


def insertReverse(head):
    if head is None or head.next is None:
        return
    # 操作头节点, 2次指针操作,头节点head.next赋值给cur, 由于头节点最终要成为尾结点,其指向为空
    cur = head.next
    head.next = None
    # 操作第二个及之后的节点,每次遍历到的节点都放到头节点处
    while cur:
        nex = cur.next
        cur.next = head
        head = cur
        cur = nex
    return head


link = LinkedList01()
link.add_at_end(1)
link.add_at_end(2)
link.add_at_end(3)
link.add_at_end(4)
link.print_link()
print("=========== after =============")
new_head = insertReverse(link.head)
print(link.head.data)
while new_head:
    print(new_head.data)
    new_head = new_head.next