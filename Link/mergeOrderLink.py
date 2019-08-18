# coding:utf-8
import sys


def merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    pre1 = head1
    pre2 = head2
    cur1 = head1.next
    cur2 = head2.next
    while cur1 and cur2:
        if cur1.data < cur2.data:
            pre1 = cur1
            cur1 = cur1.next
        else:
            pre1.next = cur2
            pre2 = cur2
            cur2 = cur2.next
            pre2.next = cur1
    return head1


def merge2(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1 = head1.next
    cur2 = head2.next
    head = None
    cur = None
    if cur1.data < cur2.data:
        head = head1
        cur = cur1
        cur1 = cur1.next

    else:
        head = head2
        cur = cur2
        cur2 = cur2.next

    while cur1 and cur2:
        if cur1.data < cur2.data:
            cur.next = cur1

            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2

            cur = cur2
            cur2 = cur2.next

    if cur1:
        cur.next = cur1
    if cur2:
        cur.next = cur2

    return head


def merge3(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    cur1 = head1
    cur2 = head2
    head = None
    cur = None
    if cur1.data < cur2.data:
        head = cur1
        cur = head
        cur1 = cur1.next
    else:
        head = cur2
        cur = head
        cur2 = cur2.next

    while cur1 and cur2:
        if cur1.data < cur2.data:
            cur.next = cur1

            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2

            cur = cur2
            cur2 = cur2.next
    if cur1:
        cur.next = cur1
    if cur2:
        cur.next = cur2
    return head


class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def constructLink(num):
    head = LNode(-1)
    cur = head
    for i in range(1, num+1):
        new_node = LNode(i)
        cur.next = new_node

        cur = cur.next
    return head


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = LNode(value)
        if self.head is None:
            self.head = new_node
            return self.head
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        return self.head


print("========before=========")
link1 = LinkedList()
link1.add(1)
link1.add(2)
link1.add(5)
link1.add(6)
link1.add(9)
link1.add(10)
link1.add(11)
c1 = link1.head
while c1:
    value1 = str(c1.data) + "->"
    sys.stdout.write(value1)
    c1 = c1.next
print("")
link2 = LinkedList()
link2.add(3)
link2.add(4)
link2.add(7)
link2.add(8)
c2 = link2.head
while c2:
    value2 = str(c2.data) + "->"
    sys.stdout.write(value2)
    c2 = c2.next
print("")
print("========after========")
new_head = merge3(link1.head, link2.head)
p = new_head
while p:
    value = str(p.data) + "->"
    sys.stdout.write(value)
    p = p.next

