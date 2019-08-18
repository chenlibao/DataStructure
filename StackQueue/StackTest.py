# -*- coding:utf-8 -*-
import unittest
from DataStructureStackQueue.Stack import Stack


class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        value = self.stack.push(10)
        self.assertEqual(value, 10)
        self.assertEqual(self.stack.top, 0)

    def test_pop1(self):
        self.stack.push(10)
        value = self.stack.pop()
        self.assertEqual(value, 10)
        self.assertEqual(self.stack.top, -1)

    def test_pop2(self):
        value = self.stack.pop()
        self.assertEqual(value, None)

    def test_get1(self):
        value = self.stack.get()
        self.assertEqual(value, None)

    def test_get2(self):
        self.stack.push(10)
        self.stack.push(20)

        value = self.stack.get()
        self.assertEqual(value, 20)
        self.assertEqual(self.stack.top, 1)

    def test_is_empty1(self):
        result = self.stack.is_empty()
        self.assertEqual(result, True)

    def test_is_empty2(self):
        self.stack.push(1)
        result = self.stack.is_empty()
        self.assertEqual(result, False)

    def test_get_size1(self):
        size = self.stack.get_size()
        self.assertEqual(size, 0)

    def test_get_size2(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        size = self.stack.get_size()
        self.assertEqual(size, 3)


if __name__ == "main":
    unittest.main()