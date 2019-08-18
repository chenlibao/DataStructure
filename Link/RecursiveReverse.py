# -*- coding:utf-8 -*-
from DataStructure.LinkedList01 import LinkedList01


def recursiveReverse(head):
    if head is None or head.next is None:
        return head
    else:
        # 先反转后边的节点：1->4->3->2
        new_head = recursiveReverse(head.next)
        # 然后将head移动到节点head.next之后
        head.next.next = head
        head.next = None
        # 参数为头结点,所以返回的为new_head新的头结点
        return new_head


link = LinkedList01()
link.add_at_end(1)
link.add_at_end(2)
link.add_at_end(3)
link.add_at_end(4)
print("============ Before ===========")
link.print_link()
print("============ after ===========")
new_head = recursiveReverse(link.head)
print(new_head.data)
while new_head:
    print(new_head.data)
    new_head = new_head.next
