# 4. Median of Two Sorted Arrays
# Hard

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        for i in range(len(nums2)):
            nums1.append(nums2[i])

        nums1 = sorted(nums1)
        merged_len = len(nums1)

        if merged_len % 2 != 0:
            mid = merged_len // 2
            return nums1[mid]
        else:
            return (nums1[merged_len//2 ] + nums1[merged_len//2 - 1]) / 2

nums1 = [-2,-1]
nums2 = [3]
obj = Solution()
result = obj.findMedianSortedArrays(nums1, nums2)
print(" Median of Two Sorted Arrays: ", result)
