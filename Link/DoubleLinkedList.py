# -*- coding:utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
            new_node.pre = p
            self.size += 1

    def print_link(self):
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            while p:
                print(p.data)
                p = p.next

    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            i = 0
            while p.next and i < index:
                p = p.next
                i = i + 1
            if i == index and p.next:
                new_node.next = p.next
                p.next = new_node
                self.size += 1
            elif i == index and p.next is None:
                new_node.next = None
                p.next = new_node
                self.size += 1
            else:
                print("Cannot find node that index is ", index)


link = DoubleLinkedList()
link.add(10)
link.add(20)
link.add(30)
link.insert(0, 100)
link.print_link()
print(link.size)