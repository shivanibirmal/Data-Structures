# 889. Construct Binary Tree from Preorder and Postorder Traversal
# Medium
#
# Return any binary tree that matches the given preorder and postorder traversals.
#
# Values in the traversals pre and post are distinct positive integers.
#
#
#
# Example 1:
#
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#
#
# Note:
#
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    pre_index, post_index = 0, 0

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(pre[self.pre_index])
        self.pre_index += 1

        if root.val != post[self.post_index]:
            root.left = self.constructFromPrePost(pre, post)
        if root.val != post[self.post_index]:
            root.right = self.constructFromPrePost(pre, post)

        self.post_index += 1

        return root

    def inorder(self, root: TreeNode):
        if (not root):
            return

        self.inorder(root.left)
        print(root.val, end = " ")
        self.inorder(root.right)

obj = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

root = obj.constructFromPrePost(pre, post)
print("Printing the tree using inorder traversal")
obj.inorder(root)

# Method of solving
#
# Recursive Solution
# Create a node TreeNode(pre[preIndex]) as the root.
#
# Becasue root node will be lastly iterated in post order,
# if root.val == post[posIndex],
# it means we have constructed the whole tree,
#
# If we haven't completed constructed the whole tree,
# So we recursively constructFromPrePost for left sub tree and right sub tree.
#
# And finally, we'll reach the posIndex that root.val == post[posIndex].
# We increment posIndex and return our root node.
#
# Complexity:
# Time O(N), as we iterate both pre index and post index only once.
# Space O(height), depending on the height of constructed tree.
