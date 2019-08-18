# -*- coding:utf-8 -*-
from DataStructure.Node import Node
from DataStructure.LinkedList_interface import Link


class LinkedList01(Link):
    def add_at_begin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            p = self.head
            self.head = new_node
            new_node.next = p
            self.size += 1

    def add_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
            self.size += 1

    def insert(self, target, value):
        new_node = Node(value)
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            while p.data != target and p.next:
                p = p.next
            if p.data == target and p.next is None:
                p.next = new_node
                self.size += 1
            elif p.data == target and p.next:
                nex = p.next
                p.next = new_node
                new_node.next = nex
            else:
                print("Cannot find ", target)

    def insert_before(self, target, value):
        new_node = Node(value)
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            pre = p
            while p.data != target and p.next:
                pre = p
                p = p.next
            if p == self.head and p.data == target:
                self.head = new_node
                new_node.next = p
                self.size += 1
            elif p.data == target:
                pre.next = new_node
                new_node.next = p
                self.size += 1
            else:
                print("Cannot find ", target)

    def delete_at_begin(self):
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            if p.next is None:
                self.head = None
                self.size -= 1
            else:
                self.head = p.next
                self.size -= 1

    def delete_at_end(self):
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            if p.next is None:
                self.head = None
                self.size -= 1
            else:
                pre = p
                while p.next:
                    pre = p
                    p = p.next
                pre.next = None
                self.size -= 1

    def delete(self, value):
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            if p.next is None and p.data == value:
                self.head = None
                self.size -= 1
            else:
                pre = p
                while p.next and p.data != value:
                    pre = p
                    p = p.next
                if p.data == value and p.next:
                    if p == self.head:
                        self.head = p.next
                        self.size -= 1
                    else:
                        pre.next = p.next
                        self.size -= 1
                elif p.data == value and p.next is None:
                    pre.next = None
                    self.size -= 1
                else:
                    print("Cannot find ", value)

    def update(self, target, value):
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            while p.data != target and p.next:
                p = p.next
            if p.data == target:
                p.data = value
            else:
                print("Cannot find ", target)

    def print_link(self):
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            while p:
                print(p.data)
                p = p.next

    def get_link(self):
        link_list = []
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            while p:
                link_list.append(p.data)
                p = p.next
        return link_list

    def get_end(self):
        if self.head is None:
            print("The link is None")
            return
        else:
            p = self.head
            while p.next:
                p = p.next
            if p.next is None:
                return p

    def get_size(self):
        return self.size

    def has_next(self):
        if self.head is None:
            print("The link is None")
            return
        else:
            p = self.head
            if p.next is not None:
                return True
            else:
                return False

    def is_belong_to_link(self, value):
        if self.head is None:
            print("The link is None")
            return False
        else:
            p = self.head
            while p.data != value and p.next:
                p = p.next
            if p.data == value:
                return True
            else:
                return False


if __name__ == "__main__":
    link = LinkedList01()
    link.add_at_end(10)
    print(link.has_next())
    link.add_at_end(20)
    link.add_at_end(30)
    link.add_at_end(40)
    link.add_at_end(50)
    link.insert_before(50, 1)
    link.delete_at_begin()
    link.delete_at_end()
    link.delete(1)
    link.update(20, 100)

    print(link.get_size())
    link.print_link()
    print(link.get_link())
    print("=========get_end()==========")
    print(link.get_end().data)
    print("============get_size================")
    print(link.get_size())
    print("=====================================")
    print(link.has_next())
    print(link.is_belong_to_link(200))
    p = link.head
    while p:
        print(p.data)
        p = p.next
