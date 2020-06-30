# 124. Binary Tree Maximum Path Sum
# Hard
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42

# Definition for a binary tree node.
from numpy import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0

        self.my_sum = -inf
        self.myMaxSum(root)

        return self.my_sum

    def myMaxSum(self, root):
        if root.left == None and root.right == None:
            self.my_sum = max(self.my_sum, root.val)
            return root.val
        if root.left:
            l = self.myMaxSum(root.left)
        else:
            l = -inf
        if root.right:
            r = self.myMaxSum(root.right)
        else:
            r = -inf

        max_var = max(l, r, l+root.val, r+root.val, l+r+root.val, root.val)
        self.my_sum = max(self.my_sum, max_var)

        return max(l+root.val, r+root.val, root.val)

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(15)
root.right.left = TreeNode(7)

obj = Solution()
max_sum = obj.maxPathSum(root)
print("Maximum Path Sum:", max_sum)
