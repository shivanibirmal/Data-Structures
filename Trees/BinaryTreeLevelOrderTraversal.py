# 102. Binary Tree Level Order Traversal
# Medium
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root == None:
            return

        q = []
        q.append(root)
        nodes_per_level = []

        while q:
            front = q[0]

            count = 0
            current_q_len = len(q)
            l = []
            while count < current_q_len:

                l.append(q[0].val)

                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)

                count += 1
                q.pop(0)

            nodes_per_level.append(l)

        return nodes_per_level

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right.right = TreeNode(5)
root.right.left = TreeNode(10)

obj = Solution()
result = obj.levelOrder(root)
print(result)
