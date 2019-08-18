# -*- coding:utf-8 -*-
from DataStructure.LinkedList01 import LinkedList01
"""
给定未排序链表,要去掉重复项,例如：
输入：1->3->1->4->4->5,
输出：1->3->4->5
思路
1. 两次遍历,外层遍历一个节点时,剩余的节点内层遍历
2. 如果相等,则删除
3. 特殊情况：head为None,或者单节点,直接返回head
"""


def removeDup(head):
    if head is None or head.next is None:
        return head
    cur = head
    while cur:
        p = cur.next
        while p:
            if cur.data == p.data:
                cur.next = p.next
            cur = cur.next
        cur = cur.next
    return head


link = LinkedList01()
print("========= before ========")
link.add_at_end(1)
link.add_at_end(3)
link.add_at_end(1)
link.add_at_end(4)
link.add_at_end(4)
link.add_at_end(5)
link.print_link()
print("========= after ========")
