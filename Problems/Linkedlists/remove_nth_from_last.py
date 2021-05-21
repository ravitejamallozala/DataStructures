"""
19. Remove Nth Node From End of List
Medium
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        forward = head
        behind = head
        count = 0
        # moving one pointer n distance from the start
        while forward and count < n:
            count += 1
            forward = forward.next
        # Starting the  second pointer from start and moving both pointers at same time
        # when the first pointer reaches last node then the second pointer will be at desired position to delete the node

        while forward and forward.next:
            behind = behind.next
            forward = forward.next

        # removing the nth element from last
        print("forward", forward, "behind: ", behind)
        if forward:
            behind.next = behind.next.next if behind.next else None
        else:
            head = head.next

        return head
