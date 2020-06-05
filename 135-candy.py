# 135. Candy

# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Example 1:

# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.

class Solution:
	# greedy solution
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n <= 1:
            return n
            
        # initial state: each kid gets one candy    
        nums = [1] * n
        # kids on upwards curve get candies
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1

        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                nums[i-1] = max(nums[i]+1, nums[i-1])
   
        return sum(nums)
        