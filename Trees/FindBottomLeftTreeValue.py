# 513. Find Bottom Left Tree Value
# Medium
#
# 871
#
# 137
#
# Add to List
#
# Share
# Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
# Example 2:
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = []
        q.append(root)

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
                # print(l)

        return l[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right.right = TreeNode(5)
root.right.left = TreeNode(10)

obj = Solution()
result = obj.findBottomLeftValue(root)
print(result)
