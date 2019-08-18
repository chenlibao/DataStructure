# -*- coding:utf-8 -*-
import unittest
from DataStructure.LinkedList01 import LinkedList01


class LinkedList01Test(unittest.TestCase):
    def setUp(self):
        self.link = LinkedList01()

    def test_add_at_begin(self):
        self.link.add_at_begin(20)
        self.link.add_at_begin(30)
        self.link.add_at_begin(40)
        p = self.link.head
        value = 40
        while p:
            self.assertEqual(p.data, value, "p.data = value")
            value = value - 10
            p = p.next

    def test_add_at_end(self):
        self.link.add_at_end(3)
        self.link.add_at_end(6)
        self.link.add_at_end(9)
        self.link.add_at_end(12)
        self.link.add_at_end(15)
        p = self.link.head
        value = 3
        while p:
            self.assertEqual(p.data, value, "p.data = value")
            value = value + 3
            p = p.next

    def test_insert(self):
        self.link.add_at_end(1)
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(5)
        self.link.add_at_end(7)

        self.link.insert(3, 4)
        self.link.insert(5, 6)
        p = self.link.head
        value = 1
        while p:
            self.assertEqual(p.data, value, "p.data == value")
            value += 1
            p = p.next

    def test_insert_before(self):
        self.link.add_at_end(1)
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(4)
        self.link.add_at_end(5)
        value = 0
        self.link.insert_before(1, 0)
        p = self.link.head
        while p:
            self.assertEqual(p.data, value, "p.data == vaule")
            value += 1
            p = p.next

    def test_delete_at_begin(self):
        self.link.add_at_end(1)
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(4)
        self.link.add_at_end(5)
        self.link.delete_at_begin()
        self.link.delete_at_begin()
        value = 3
        p = self.link.head
        while p:
            self.assertEqual(p.data, value, "p.data == value")
            value += 1
            p = p.next

    def test_delete_at_end(self):
        self.link.add_at_end(1)
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(4)
        self.link.add_at_end(50)
        self.link.delete_at_end()
        value = 1
        p = self.link.head
        while p:
            self.assertEqual(p.data, value, "p.data == value")
            value += 1
            p = p.next

    def test_delete_at_end_size(self):
        self.link.add_at_end(1)
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(4)
        self.link.add_at_end(50)
        self.link.delete_at_end()
        self.link.delete_at_end()
        size = self.link.size
        self.assertEqual(size, 3)

    def test_update(self):
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(6)
        self.link.add_at_end(8)
        self.link.add_at_end(10)
        self.link.update(3, 4)
        value = 2
        p = self.link.head
        while p:
            self.assertEqual(p.data, value, "p.data == value")
            value += 2
            p = p.next

    def test_get_link(self):
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(6)
        self.link.add_at_end(8)
        self.link.add_at_end(10)
        link_list = self.link.get_link()
        i = 0
        p = self.link.head
        while p:
            self.assertEqual(p.data, link_list[i], "p.data = link_list[i]")
            i = i + 1
            p = p.next

    def test_get_end(self):
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(6)
        self.link.add_at_end(8)
        self.link.add_at_end(10)
        end = self.link.get_end()
        self.assertEqual(end.data, 10, "end.data == 10")

    def test_get_size(self):
        self.link.add_at_end(2)
        self.link.add_at_end(3)
        self.link.add_at_end(6)
        self.link.add_at_end(8)
        self.link.add_at_end(10)
        size = self.link.get_size()
        self.assertEqual(size, 5)


if __name__ == "__main__":
    unittest.main()
