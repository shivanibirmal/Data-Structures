# 384. Shuffle an Array
# Medium

# Shuffle a set of numbers without duplicates.

# Example:

# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();

# // Resets the array back to its original configuration [1,2,3].
# solution.reset();

# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        new_list = self.nums[:]
        random.shuffle(new_list)
        return new_list

# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
print("Given array:", nums)

shuffled_array = obj.shuffle()
print("Shuffle:", shuffled_array)

reseted_array = obj.reset()
print("Reset:", reseted_array)

shuffled_array = obj.shuffle()
print("Shuffle:", shuffled_array)

# param_1 = obj.reset()
# param_2 = obj.shuffle()
