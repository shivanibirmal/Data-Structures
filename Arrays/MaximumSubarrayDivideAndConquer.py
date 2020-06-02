from typing import List
import math

class Solution:
    def maxCrossingSum(self, nums: List[int], low: int, high: int)-> int:
        mid = (low + high) // 2

        max_to_left = - math.inf
        sum1 = 0
        sum2 = 0
        max_to_right = - math.inf

        for i in range(mid, low- 1, -1):
            sum1 += nums[i]
            if(sum1 > max_to_left):
                max_to_left = sum1

        for i in range(mid+1, high+1):
            sum2 += nums[i]
            if(sum2 > max_to_right):
                max_to_right = sum2

        max_crossing = max_to_left + max_to_right
        return max_crossing

    def divideAndConquer(self, nums: List[int], low: int, high: int)-> int:
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        max_left = self.divideAndConquer(nums, low, mid)
        max_right = self.divideAndConquer(nums, mid+1, high)
        max_crossing = self.maxCrossingSum(nums, low, high)

        return max(max_left, max_right, max_crossing)

nums = [-2,-1]
obj = Solution()

max = obj.divideAndConquer(nums, 0, len(nums)-1)
print("Dynamic Programming:", max)
