# -*- coding:utf-8 -*-
from DataStructure.LinkedList import LinkedList
"""
实现单链表逆序
思路:
分为pre, cur, nex三个变量,作为每次操作节点的指针
从单个节点来说,单个节点指针有2次变化,先把指针cur.next赋值给nex（nex=cur.next),再把指针cur.next指向pre（cur.next=pre)
同时, 准备下一个节点操作, 移动cur到下个节点,当前节点赋值给前一个,下一个节点赋值给当前节点（pre=cur,cur=nex)
当节点是尾结点时, 将其赋值给头结点（head=cur）
"""


def reverse(head):
    # 头节点为空或者为单节点,直接返回
    if head is None or head.next is None:
        return head
    else:
        # 移动cur到头节点
        cur = head
        # 操作当前节点指针, 2次操作
        nex = cur.next
        cur.next = None

        # 移动cur到下一个节点
        pre = cur
        cur = nex
        # 循环操作节点
        while cur.next:
            # 操作当前节点指针, 2次操作
            nex = cur.next
            cur.next = pre
            # 移动cur到下一个节点
            pre = cur
            cur = nex
        # 最后一个操作节点, 指针指向其前一个pre,同时将其设为头节点
        cur.next = pre
        head = cur
    return head


link = LinkedList()
print("=========== before =============")
link.add(1)
link.add(2)
link.add(3)
link.add(4)
link.print_list()
print("=========== after ==============")
new_head = reverse(link.head)
while new_head:
    print(new_head.data)
    new_head = new_head.next
