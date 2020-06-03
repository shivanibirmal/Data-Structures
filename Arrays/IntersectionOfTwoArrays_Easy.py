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
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        output = []

        i = 0
        j = 0

        while(i < len1 and j < len2):
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return output

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
result = obj.intersect(nums1, nums2)
print("Intersection of given arrays: ", result)

# Method of solving

# 1. sort both the Arrays
# 2. let there be 2 pointers i and j for the 2 respective Arrays
# 3. increment i if nums1[i] is smaller
# 4. increment j if nums2[j] is smaller
# 4. if nums1[i] is equal to nums2[j], then add it to the output list
