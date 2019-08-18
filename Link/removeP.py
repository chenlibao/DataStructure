# -*- coding:utf-8 -*-
from DataStructure.LinkedList import LinkedList, Node
import sys


def removeP(p):
    if p is None or p.next is None:
        return False
    p.data = p.next.data
    tmp = p.next
    p.next = tmp.next
    return True


link = LinkedList()
link.add(1)
link.add(2)
link.add(3)
link.add(4)
link.add(5)
link.add(6)
cur = link.head
while cur:
    value = str(cur.data) + "->"
    sys.stdout.write(value)
    cur = cur.next

print()
print("========remove node 3======")
p = link.head.next.next
removeP(p)
cur2 = link.head
while cur2:
    value = str(cur2.data) + "->"
    sys.stdout.write(value)
    cur2 = cur2.next
