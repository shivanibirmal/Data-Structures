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

        left_subtree = []
        right_subtree = []

        if root is None:
            return True
        else:
            self.giveLeftSubtree(root.left, left_subtree)
            self.giveRightSubtree(root.right, right_subtree)

        print("left_subtree:", left_subtree)
        print("right_subtree:", right_subtree)

        if left_subtree == right_subtree:
            return True
        else:
            return False

    def giveLeftSubtree(self, node, left_subtree):

        if node == None:
            left_subtree.append("")

        else:
            self.giveLeftSubtree(node.left, left_subtree)
            self.giveLeftSubtree(node.right, left_subtree)
            left_subtree.append(node.val)

    def giveRightSubtree(self, node, right_subtree):

        if node == None:
            right_subtree.append("")
        else:
            self.giveRightSubtree(node.right, right_subtree)
            self.giveRightSubtree(node.left, right_subtree)
            right_subtree.append(node.val)
