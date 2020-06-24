# 199. Binary Tree Right Side View
# Medium
#
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return

        q = []
        q.append(root)
        l = []

        while q:
            front = q[0]

            count = 0
            current_q_len = len(q)
            while count < current_q_len:

                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)

                count += 1
                popped_element = q.pop(0)

            l.append(popped_element.val)

        return l


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right.right = TreeNode(5)
root.right.left = TreeNode(10)

obj = Solution()
result = obj.rightSideView(root)
print(result)
