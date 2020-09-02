
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
my solution
class Solution:
    #     def __init__(self):
    #         self.prev = None
    #         self.rit = False
    #         self.lef = False

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:  # key == root.val

            if root.left:
                root.val = root.left.val
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                root.val = root.right.val
                root.right = self.deleteNode(root.right, root.val)
            else:
                root = None
        return root

"""