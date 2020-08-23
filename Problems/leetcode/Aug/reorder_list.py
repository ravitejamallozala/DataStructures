"""
Reorder List
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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        #finding middle of Linked list
        while fast:

            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        print(slow.val)
        print(fast.val)
        # reversing second half of linked list
        prev = None
        temp = slow.next
        while temp:
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        slow.next = prev
        print("after reversal\n")
        display(head)
        # assigning Alternate Values:
        head1 = head
        while slow != head1:
            prev = slow
            slow = slow.next

            main_next = head1.next
            head1.next = slow
            rev_next = slow.next if slow else None
            slow.next = main_next
            prev.next = rev_next
            slow = prev
            head1 = main_next



# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4,5]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)

    s = Solution()
    s.reorderList(root)
    display(root)
