# 384. Shuffle an Array

# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

from random import randint
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        result = list(self.nums)
        for i in range(len(result)):
            r = randint(0, i)
            result[i], result[r] = result[r], result[i]
            print(result)
        return result

# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5]
print(Solution(nums).shuffle())
# param_1 = obj.reset()
# param_2 = obj.shuffle()
