# 129. Sum Root to Leaf Numbers
# Medium
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
#
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        if root == None:
            return 0

        q = []
        q.append(tuple((root,root.val)))
        list_of_paths = []

        my_sum = 0
        while q:
            current_q_len = len(q)
            count = 0
            while count < current_q_len:
                (popped_element, number_formed) = q.pop(0)

                if popped_element.left:
                    q.append(tuple((popped_element.left, number_formed*10 + popped_element.left.val)))

                if popped_element.right:
                    q.append(tuple((popped_element.right, number_formed*10 + popped_element.right.val)))

                if popped_element.left == None and popped_element.right == None:
                    list_of_paths.append(number_formed)

                count += 1

        return sum(list_of_paths)

root = TreeNode(1)
root.left = TreeNode(9)
root.right = TreeNode(2)
root.right.right = TreeNode(1)
root.right.left = TreeNode(7)

obj = Solution()
my_sum = obj.sumNumbers(root)
print("Sum of Root to Leaf Numbers is ", my_sum)
