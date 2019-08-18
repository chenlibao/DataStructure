# coding:utf-8
from DataStructure.LinkedList import LinkedList, Node

"""
1. 如果两链表交叉，尾结点相同
2. 链表长度n1, n2
3. 另长链表先出发|n1-n2|步，则第一次相遇时,就是交叉的点
"""


def isIntersect(head1, head2):
    if head1 is None or head2 is None or head1.next is None or head2.next is None:
        return None
    end1 = head1.next
    end2 = head2.next
    n1 = 0
    n2 = 0
    while end1.next:
        end1 = end1.next
        n1 += 1
    while end2.next:
        end2 = end2.next
        n2 += 1
    if end1 == end2:
        if n1 > n2:
            while n1 > n2:
                head1 = head1.next
                n1 -= 1
        else:
            while n1 < n2:
                head2 = head2.next
                n2 -= 1
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1
    else:
        return None


test_head1 = Node(None)
test_head2 = Node(None)

cur1 = test_head1
i = 1
tmp = None
p = None
while i < 8:
    tmp = Node(i)
    tmp.next = None
    cur1.next = tmp
    cur1 = tmp
    if i == 5:
        p = tmp
    i += 1

cur2 = test_head2
j = 1
while j < 5:
    tmp = Node(j)
    cur2.next = tmp
    cur2 = tmp
    j += 1
cur2.next = p


interNode = isIntersect(test_head1, test_head2)
print(interNode)
