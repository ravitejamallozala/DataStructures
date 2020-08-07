#   Vertical Order Traversal of a Binary Tree
# AUG 8th  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        from collections import OrderedDict
        self.ans_dict = OrderedDict()

    def inorder(self, head: TreeNode, level, hlevel):
        if not head:
            return
        left = self.inorder(head.left, level - 1, hlevel + 1)
        # print("here: ",head.val)
        if level in self.ans_dict:
            # print("updating: ",head.val, " level: ", level, "dict", self.ans_dict)
            self.ans_dict[level].append((head.val, hlevel))
        else:
            # print("Insertng: ",head.val, " level: ", level, "dict", self.ans_dict)
            self.ans_dict[level] = [(head.val, hlevel)]
        right = self.inorder(head.right, level + 1, hlevel + 1)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.inorder(root, 0, 0)
        ans = []
        print("final ", self.ans_dict)
        for key in sorted(self.ans_dict):
            vals = self.ans_dict.get(key)

            vals = sorted(vals, key=lambda ele: (ele[1], ele[0]))
            ans.append([x[0] for x in vals])
        return ans


