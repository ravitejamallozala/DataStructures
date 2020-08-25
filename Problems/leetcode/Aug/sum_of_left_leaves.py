"""
 Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    # from_direction = 1(left) , 0(right)
    def dfs(self, root, direction):
        if not root:
            return
        if direction == 1 and not root.left and not root.right:
            self.sum += root.val

        self.dfs(root.right, 0)
        self.dfs(root.left, 1)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.dfs(root, None)
        return self.sum

