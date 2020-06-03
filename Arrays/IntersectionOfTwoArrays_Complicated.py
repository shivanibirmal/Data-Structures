# 350. Intersection of Two Arrays II
# Easy
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.


# THIS IS A COMPLICATED APPROACH. REFER TO THE EASY AND BETTER APPROACH IN IntersectionOfTwoArrays_Easy.py

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        output = []

        if (len1 < len2):
            for i in range(len1):
                firstOccurence  = self.binarySearch(nums2, nums1[i])

                if firstOccurence != -1:
                    output.append(nums2[firstOccurence])
                    nums2.pop(firstOccurence)

        else:
            for i in range(len2):
                firstOccurence  = self.binarySearch(nums1, nums2[i])

                if firstOccurence != -1:
                    output.append(nums1[firstOccurence])
                    nums1.pop(firstOccurence)
        return output

    def binarySearch(self, nums: List[int], searchElement: int)->int:

        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = (low + high) // 2

            if searchElement == nums[mid]:
                print(searchElement, "found  at",mid)
                return mid

            elif (searchElement > nums[mid]):
                low = mid+1
            elif (searchElement < nums[mid]):
                high = mid - 1
        return -1

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
result = obj.intersect(nums1, nums2)
print("Intersection of given arrays: ", result)
