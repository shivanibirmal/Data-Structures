# 739. Daily Temperatures
# Medium

# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
# 
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        result = []
        my_stack = []
        for i in range(len(T)-1):
            # print("current:", T[i])
            if T[i+1] > T[i]:
                result.append(1)
            else:
                j = i+1
                greater_found = False
                count = 0
                while j <= len(T) - 1 :
                    if T[j] <= T[i]:
                        count += 1
                        greater_found = False
                    elif T[j] > T[i]:
                        greater_found = True
                        break
                    j += 1

                if greater_found == False:
                    result.append(0)
                else:
                    result.append(count+1)

            # print("list after every iter:", result)
        result.append(0)

        return result

s = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution()
result = obj.dailyTemperatures(s)
print("Result:", result)
