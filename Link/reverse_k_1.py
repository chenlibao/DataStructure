# coding:utf-8
from DataStructure.LinkedList import LinkedList, Node


def reverse(head):
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


def reverseK(head, k):
    if head is None or head.next is None or k < 2:
        return head
    pre = head  # 头节点
    begin = head.next   # 链表第一个节点
    i = 1
    while begin:
        end = begin
        while i < k:    # 找到末尾值,i=k跳出循环,end不为空,end.next可能为空
            if end.next:
                end = end.next
            else:
                return head    # 剩余节点不足k个,直接返回链表
            i += 1
        nex = end.next
        end.next = None     # 断开链表,为逆序做准备
        pre.next = reverse(begin)   # 上一个的尾指向逆序后的头
        begin.next = nex            # 逆序后的尾连上之前断开的链表

        pre = begin     # 移动,进行下一轮操作
        begin = nex
        i = 1           # i重置为1
    return head


def reverse_k(head, k):
    if head is None or head.next is None or k < 2:
        return head
    pre = head
    begin = head.next
    i = 1
    while begin:
        end = begin
        while i < k and end.next:
            end = end.next
            i += 1
        if i == k:
            nex = end.next
            end.next = None
            pre.next = reverse(begin)
            begin.next = nex

            pre = begin
            begin = nex
            i = 1
        else:
            return head
    return head


link = LinkedList()
print("=============before=========")
link.add(1)
link.add(2)
link.add(3)
link.add(4)
link.add(5)
link.add(6)
link.add(7)
link.add(8)
link.add(9)
link.print_list()
print("=============after=========")
# 需要构造头节点
head_node = Node(0)
head_node.next = link.head
new_head = reverseK(head_node, 4)
# 遍历时,跳过头节点，从第一个节点开始遍历
p = new_head.next
while p:
    print(p.data)
    p = p.next
