"""
Partition List
Leetcode - 86
https://leetcode.com/problems/partition-list
Topic: Linked List
"""
# # Definition for singly-linked list.
# class ListListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#

import math


# Representation of a ListNode
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None


# Function to insert ListNode
def insert(root, item):
    temp = ListNode(item)

    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp

    return root


def display(root):
    while (root != None):
        print(root.val, end=" ")
        root = root.next


def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])

    return root


class Solution:
    def partition(self, head: ListNode, x: int):
        print("Here")
        main = head
        prev = None
        nex = None
        old = None
        while (head):
            print("val is :", head.val)
            if prev is None and head.val < x and old is None:
                prev = head
            print("prev is  ", prev)
            if head.val >= x:
                pass
            else: #head.val < x:

                if old is not None:
                    old.next = head.next if head.next is not None else None
                    if not prev:
                        head.next = main
                        main = head
                    else:
                        head.next = prev.next
                        prev.next = head
                        prev = prev.next
                        head = old
                        display(main)

            print("Before moving head to next")
            old = head
            head = head.next
        display(main)
        return main

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        nex = head
        while head:
            nex = head.next
            head.next = prev
            prev = head
            # if nex is None:
            #     break
            head = nex
        print("Final ans")
        display(prev)
        return prev



# Driver code
if __name__ == '__main__':
    arr = [1,2,3,4, 5]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)
    print()
    s = Solution()
    # s.partition(root, 4)
    s.reverseList(root)