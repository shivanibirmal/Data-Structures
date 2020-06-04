# 1441. Build an Array With Stack Operations
# Easy

# Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.
#
# Build the target array using the following operations:
#
# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.
#
# Return the operations to build the target array.
#
# You are guaranteed that the answer is unique.

# Function buildArraySolution2 is better approach

from typing import List

class Solution:
    def buildArraySolution1(self, target: List[int], n: int) -> List[str]:

        push = "Push"
        pop = "Pop"
        target_len = len(target)
        output = []
        i = 0

        count = 1
        while i < n and count <= n:
            # print("i", i)
            # print("count:", count)

            if i >= target_len:
                break

            if target[i] == count:
                output.append(push)
                i += 1
                count += 1
            else:
                output.append(push)
                output.append(pop)
                count += 1
        return output

    def buildArraySolution2(self, target: List[int], n: int) -> List[str]:
        target_len = len(target)
        output = []
        temp = []

        #create a list from 1 to last element of target array in reverse order so that we can start popping
        #from last element which would start from one in our case

        for i in range(target[target_len-1],-1,-1):
            temp.append(i+1)

        while len(temp)-1 != 0:
            if temp.pop() not in target:
                output.append("Push")
                output.append("Pop")
            else:
                output.append("Push")
        return output

target = [1,3]
n = 3
obj = Solution()
result1 = obj.buildArraySolution1(target, n)
result2 = obj.buildArraySolution2(target, n)
print("Output: ", result1)
print("Output: ", result2)
