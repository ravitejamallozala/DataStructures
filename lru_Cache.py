# LRU cache
"""
Operations
1. search -> update the Rank
2. insert
3. delete
4. size-of
Datastructure
linkedlist -> head & tail (deque
dict = {
    "key": 0
}
"""
from collections import deque


class LRUcache:
    def __init__(self, capacity):
        self.lru = deque()
        self.size = 0
        self.capacity = capacity
        self.cache_ele = {}

    def update_size(self, size):
        self.size = size

    def check_size(self):
        if self.size <= self.capacity:
            return True
        return False

    def delete_lru(self):
        ele = self.lru.pop()
        self.update_size(self.size + -1)
        del self.cache_ele[ele]

    def insert_lru(self, ele):
        if self.check_size():
            self.lru.appendleft(ele)
        else:
            self.delete_lru()
            self.lru.appendleft(ele)
        self.cache_ele[ele] = True
        self.update_size(self.size + 1)

    def search_lru(self, ele):
        if self.cache_ele[ele]:
            self.lru.remove(ele)
        self.insert_lru(ele)
        return ele


# Driver code
s = LRUcache(4)
s.insert_lru(1)
s.insert_lru(2)
s.insert_lru(3)
s.insert_lru(4)
s.insert_lru(5)
s.insert_lru(6)
# s.search_lru(6)
# s.search_lru(6)
print(s.lru)
