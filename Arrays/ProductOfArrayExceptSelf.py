# 238. Product of Array Except Self
# Medium
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

from typing import List
def productExceptSelf( nums: List[int]):

    nums_length = len(nums)

    l = [1] * nums_length
    r = [1] * nums_length

    output = [1] * nums_length

    #find the product of elements to the left of the ith index

    for i in range(1, nums_length):
        l[i] = l[i-1] * nums[i-1]

    #find the product of elements to the right of the ith index

    for i in range(nums_length-2, -1, -1):
        r[i] = r[i+1] * nums[i+1]

    #find the product of every ith element in the right
    #array with ith element in the left array

    for i in range (nums_length):
        output[i] = l[i] * r[i]

    return output

nums = [1,2,3,4]
result = productExceptSelf(nums)
print("Product of array except self:", result)
