# 101. Symmetric Tree
# Easy
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        return self.checkIfMirror(root, root)

    def checkIfMirror(self, t1, t2):

        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        else:
            return t1.val == t2.val and self.checkIfMirror(t1.left, t2.right) and self.checkIfMirror(t1.right, t2.left)
