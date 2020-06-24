# 70. Climbing Stairs
#
# Easy

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:

        fibo = [None] * (n+1)
        fibo[0] = 1
        fibo[1] = 1

        i = 2
        while i <= n:
            fibo[i] = fibo[i-1] + fibo[i-2]
            # print(fibo)
            i += 1

        return fibo[-1]

obj = Solution()
n1 = 6
result = obj.climbStairs(n1)
print("There are", result, "ways to climb", n1, "stairs")

n2 = 19
result = obj.climbStairs(n2)
print("There are", result, "ways to climb", n2, "stairs")

# Method of solving

# A fibonacci pattern is generated while calculating the number of ways to climb stairs starting from 1.
# try finding all combinations manually for small numbers to identify this pattern
# given a number, split it in 2's. that would be one way. then split every 2 in that result into 1,1 one by one
# and try rotating that result by 1 till we get the original result. every rotation would be one way of climbing the stairs.
# in this way, keep on splitting all the 2's one by one and rotate the result. this will continue till we get all 1's in
# the result.
