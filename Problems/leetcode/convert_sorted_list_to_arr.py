"""
109. Convert Sorted List to Binary Search Tree
Medium
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convert_bst(self, arr, low, high):
        # arr: Sorted array
        # print("\nlow: ",low, "high ", high)
        if low <= high:
            mid = (low + high) // 2
            # print("mid ", mid)
            tree_head = TreeNode(arr[mid])
            tree_head.left = self.convert_bst(arr, low, mid - 1)
            tree_head.right = self.convert_bst(arr, mid + 1, high)
            return tree_head
        return None

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Converting into List
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        tree_head = self.convert_bst(arr, 0, len(arr) - 1)
        return tree_head
