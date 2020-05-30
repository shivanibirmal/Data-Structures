# 448. Find All Numbers Disappeared in an Array
# Easy
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


def findDisappearedNumbers(nums):
    nums2 = []
    for i in range(1, len(nums)+1):
        nums2.append(i)
    return list(set(nums2) - set(nums) & set(nums2)) # use '&' for intersect, '|' for union

#               OR


    s1 = set(range(1, len(nums)+1))
    print(s1)
    s2 = set(nums)
    print(s2)
    return list(s1 - s2)


nums = [1,1,1]
print ("Input array:", nums)
res = findDisappearedNumbers(nums)
print("Disappeared numbers", res)


# explanation: A = nums
# B = array[1,n] -- n inclusive
# A intersect B --> gives common elements
# B - Common elements --> gives disappeared elements
