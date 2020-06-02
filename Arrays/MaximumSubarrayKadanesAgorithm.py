from typing import List
import math

class Solution:
    def kadanesAlgorithm(self, nums: List[int]):
        # here, the basic idea is to find the max subarray ending at every index.
        # It is either the element at that index or the element at that index plus the previous max subarray
        # refer: https://www.youtube.com/watch?v=86CQq3pKSUw

        max_current = nums[0]
        max_global = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            # print("max_current:", max_current)
            if(max_current > max_global):
                max_global  = max_current

        print("Kadanes Algorithm:", max_global)

nums = [-2,-1]
obj = Solution()
obj.kadanesAlgorithm(nums)
