# -*- coding:utf-8 -*-


class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        self.queue.append(value)
        self.rear += 1

    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print("The queue is empty")

    def get_size(self):
        return self.rear - self.front

    def is_empty(self):
        return self.front == self.rear

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            return None
        return self.queue[self.rear-1]
