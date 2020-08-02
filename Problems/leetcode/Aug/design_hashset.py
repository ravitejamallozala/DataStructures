# Leetcode AUG Challenge
#

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        self.arr = []

    def add(self, key: int) -> None:
        if key in self.hash:
            self.hash[key] += 1
        else:
            self.hash[key] = 1

    def remove(self, key: int) -> None:
        if key in self.hash:
            del self.hash[key]
            # else:
            #     self.hash[key] -= 1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hash

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#  { 1: 1 2:2  }
