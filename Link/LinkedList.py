# -*- coding:utf-8 -*-


# 每个节点包含Node.data和Node.next属性,构造器可以传入值
# 新建一个节点next属性可以为空,但必须传入值data,哪怕传入的data为None, 也必须传入
class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


# 单链表,包含属性头节点LinkedList.head和链表长度LinkedList.size
# 构造器中, 单链表默认是空的,所以头结点为空,长度为空
# 其添加节点的方式不能通过构造器来添加,需要通过函数来添加
class LinkedList:
    head = None
    size = 0

    def __init__(self):
        self.head = None
        self.size = 0

    # 只要节点不为空,通过while循环,调用p.data和p.next即可实现遍历链表
    def print_list(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next
    """
    def add_node(self, new_data):
        new_node = Node(new_data)
        if self.size == 0:
            self.head = new_node
            self.size = self.size + 1
        else:
            p = self.head
            # while直接用p.next，而不用p，头结点已经是不为空了，这样也省去判断，如果用p，
            # 最后跳出循环时，其结果的p是一个None值，而p.next的方式，跳出循环后，p.next是None值
            # 但p不是None值
            while p.next is not None:
                p = p.next
            p.next = new_node
            self.size = self.size + 1
    """

    def add(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = new_node
        self.size += 1

    def insert(self, a, new_data):
        new_node = Node(new_data)
        if self.size == 0:
            print("The LinkedList is none")
        else:
            p = self.head
            # 当p值为a或者p.next为None时，跳出循环, 这里的循环，一定要用p.next不能用p is not None
            while p.data != a and p.next:
                p = p.next
            if p.next is None and p.data == a:
                p.next = new_node
                self.size += 1
            elif p.next and p.data == a:
                new_node.next = p.next
                p.next = new_node
                self.size += 1
            elif p.next is None and p.data != a:
                print("Cannot find a")

    def delete(self, del_data):
        if self.head is None:
            print("The link list is None")
        else:
            p = self.head
            pre = p
            while p.data != del_data and p.next:
                pre = p
                p = p.next
            if p == self.head and p.data == del_data and p.next is None:
                self.head = None
                self.size -= 1
            elif p == self.head and p.data == del_data and p.next:
                self.head = p.next
                self.size -= 1
            elif p.data == del_data and p.next is None:
                pre.next = None
                self.size -= 1
            elif p.data == del_data and p.next:
                pre.next = p.next
                self.size -= 1
            else:
                print("cannot find ", del_data)

    def delete_at_begin(self):
        if self.head is None:
            print("The link is None")
        elif self.head.next:
            self.head = self.head.next
            self.size -= 1
        else:
            self.head = None
            self.size -= 1

    def delete_at_end(self):
        if self.head is None:
            print("The link is None")
        elif self.head.next is None:
            self.head = None
            self.size -= 1
        else:
            p = self.head
            pre = p
            while p.next:
                pre = p
                p = p.next
            pre.next = None
            self.size -= 1

    def update(self, a, b):
        if self.head is None:
            print("The link is None")
        else:
            p = self.head
            while p.data != a and p.next:
                p = p.next
            if p.data == a:
                p.data = b
                return
            else:
                print("There is no ", a)


if __name__ == "__main__":
    link = LinkedList()
    print("============origin data============")
    link.add(1)
    link.add(2)
    link.add(3)
    link.add(4)
    link.add(4)
    link.add(5)
    link.print_list()
    print("============insert(4, 10)============")
    link.insert(4, 10)
    link.print_list()
    print("============delete(1) ============")
    link.delete(1)
    link.print_list()
    print("============ update(1, 25) ============")
    link.update(1, 25)
    link.print_list()
    print("============ delete_at_begin()============")
    link.delete_at_begin()
    link.print_list()
    print("============ delete_at_end() ===============")
    link.delete_at_end()
    link.delete_at_end()
    link.delete_at_end()
    link.delete_at_end()
    link.delete_at_end()
    link.delete_at_end()
    link.print_list()
