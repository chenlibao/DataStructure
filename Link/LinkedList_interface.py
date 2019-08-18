# -*- coding:utf-8 -*-


# link interface
class Link:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_at_begin(self, value):
        pass

    def add_at_end(self, value):
        pass

    def insert(self, target, value):
        pass

    def insert_before(self, target, value):
        pass

    def delete_at_begin(self):
        pass

    def delete_at_end(self):
        pass

    def delete(self, value):
        pass

    def update(self, target, value):
        pass

    def print_link(self):
        pass

    def get_link(self):
        pass

    def get_end(self):
        pass

    def get_size(self):
        return self.size

    def has_next(self):
        pass

    def is_belong_to_link(self, value):
        pass
