#DOES NOT WORK FOR ALL CASES

from typing import List
import math

class Solution:
    def maxSubArrayMethod1(self, nums: List[int]):
        max_sum = 0

        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                sum = 0
                for k in range(i,j+1):
                    sum += nums[k]
                max_sum = max(max_sum, sum)


        print("Brute Force:", max_sum)

nums = [-2,-1]
obj = Solution()
obj.maxSubArrayMethod1(nums)
