"""
Path Sum III
AUG 8th
Topic Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def search_sum(self, head, val, sum):
        if not head:
            return

        if val + head.val == sum:
            self.count += 1
        self.search_sum(head.right, val + head.val, sum)
        self.search_sum(head.left, val + head.val, sum)

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return self.count

        def bfs(root):
            queue = [root]
            while queue:
                ele = queue.pop(0)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                self.search_sum(ele, 0, sum)

        bfs(root)
        return self.count
