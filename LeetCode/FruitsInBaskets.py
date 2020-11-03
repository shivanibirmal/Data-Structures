# 904. Fruit Into Baskets
# Medium
#
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following steps:
#
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?

# Example 1:
#
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# Example 2:
#
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# Example 3:
#
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# Example 4:
#
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
#
#
# Note:
#
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
from typing import List

class Solution:
    def totalFruit(self, tree: List[int]):
        i = 0
        j = 1

        if len(tree) == 1:
            return 1

        b1 = []
        b2 = []
        global_count = 0

        while i < len(tree):
            if j == len(tree):
                break
            if len(b1) == 0 or tree[i] == b1[-1]:
                b1.append(tree[i])
            else:
                if len(b2) == 0 or tree[i] == b2[-1]:
                    b2.append(tree[i])

            while j < len(tree):
                was_appended = False
                if len(b1) == 0 or tree[j] == b1[-1]:
                    b1.append(tree[j])
                    j += 1
                    was_appended = True
                else:
                    if len(b2) == 0 or tree[j] == b2[-1]:
                        b2.append(tree[j])
                        j += 1
                        was_appended = True
                if was_appended == False:
                        i = j - 1
                        global_count = max(global_count, len(b2) + len(b1))
                        b1.clear()
                        b2.clear()
                        break

        global_count = max(global_count, len(b2) + len(b1))
        return global_count

tree = [0,1,6,6,4,4,6]
solution = Solution()
print("tree:", tree)
total_fruits = solution.totalFruit(tree)
print("total fruits:",total_fruits)
