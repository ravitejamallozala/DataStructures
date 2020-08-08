"""
445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        temp1 = l1
        temp2 = l2
        while (temp1):
            num1 = num1 * 10 + temp1.val
            temp1 = temp1.next

        while (temp2):
            num2 = num2 * 10 + temp2.val
            temp2 = temp2.next
        total = num1 + num2
        print(total)
        if total is 0:
            return ListNode(0, None)
        temp = None
        while total:
            num = total % 10
            print("num is :", num)
            if not temp:
                temp = ListNode(num, None)
            else:
                temp = ListNode(num, temp)
            print("total is ", total)
            total = total // 10
        return temp
