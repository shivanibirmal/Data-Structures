# 110. Balanced Binary Tree
# Easy
#
# 2168
#
# 165
#
# Add to List
#
# Share
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root) != -1

    def check(self, root: TreeNode)  -> int :
        if not root:
            return 0

        left = self.check(root.left)
        if left == -1:
            return -1
        right = self.check(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(15)
root.right.left = TreeNode(7)

obj = Solution()
result = obj.isBalanced(root)
print(result)
