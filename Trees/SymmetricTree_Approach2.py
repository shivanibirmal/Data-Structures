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
        else:
            nodes_per_level = []
            curr_list = []
            next_list = []

            curr_list.append(root)
            nodes_per_level.append(curr_list[0].val)

            while curr_list:
                i = 0
                level = []
                while (i < len(curr_list) ):

                    if curr_list[i] != "" and curr_list[i].left:
                        next_list.append(curr_list[i].left)
                        level.append(curr_list[i].left.val)
                    else:
                        next_list.append("")
                        level.append("")

                    if curr_list[i]  != "" and curr_list[i].right:
                        next_list.append(curr_list[i].right)
                        level.append(curr_list[i].right.val)
                    else:
                        next_list.append("")
                        level.append("")

                    i += 1

                if level.count("") != len(level):
                    nodes_per_level.append(level)
                    curr_list = next_list[:]
                    next_list = []

                    l = 0
                    r = len(level) - 1
                    while(l < r):
                        if level[l] == level[r]:
                            l += 1
                            r -= 1
                        else:
                            return False
                else:
                    break

            return True
