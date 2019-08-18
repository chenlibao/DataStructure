# -*- coding:utf-8 -*-
from collections import deque


class LRU:
    def __init__(self, maxsize):
        self.cacheSize = maxsize
        self.queue = deque()
        self.hashSet = set()

    def is_full(self):
        return len(self.queue) == self.cacheSize

    def enqueue(self, pageNum):
        if self.is_full():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        self.hashSet.add(pageNum)

    def accessQueue(self, pageNum):
        if pageNum not in self.hashSet:
            self.enqueue(pageNum)
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)

    def printQueue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())


if __name__ == "__main__":
    lru = LRU(4)
    lru.accessQueue(1)
    lru.accessQueue(2)
    lru.accessQueue(3)
    lru.accessQueue(4)
    lru.accessQueue(5)
    lru.accessQueue(6)
    lru.printQueue()