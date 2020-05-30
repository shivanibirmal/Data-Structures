# 442. Find All Duplicates in an Array

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

def findDuplicates( nums):
    nums = sorted(nums)
    i=0
    j=1
    result = []
    n = len(nums)
    while(j < n):
        if(nums[i] == nums[j]):
            result.append(nums[i])
        i += 1
        j += 1
    return result

nums = [4,3,2,7,8,2,3,1]
print("Input array:", nums)
result = findDuplicates( nums)
print("Duplicates:",result)
