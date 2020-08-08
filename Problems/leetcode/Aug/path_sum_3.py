"""
AUG 8th
Topic Binary Tree
=> Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
