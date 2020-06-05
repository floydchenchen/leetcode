# 683. K Empty Slots

# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days.
# In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place
# where the flower will open in that day.
#
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x,
# where i and x will be in the range from 1 to N.
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming,
# and also the number of flowers between them is k and these flowers are not blooming.
#
# If there isn't such day, output -1.
#
# Example 1:
# Input:
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
# Example 2:
# Input:
# flowers: [1,2,3]
# k: 1
# Output: -1

# 补充说明
# flowers[i]: 在第i天，在flowers[i]这个position开花
# 问哪天有两朵开的花，中间间隔k朵没开的花(k empty slots)

import math
class Solution:

    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        days = [0] * n
        for i in range(n):
            days[flowers[i] - 1] = i + 1

        left, right, result = 0, k + 1, math.inf
        i = 1
        while i < n and right < n:
            while i < n and days[left] < days[i] and days[right] < days[i]:
                i += 1
            if i == right:
                result = min(result, max(days[left], days[right]))
            left = i
            right = k + left + 1
            i += 1

        return -1 if result == math.inf else result






sol = Solution()
# flowers =  [6,5,8,9,7,1,10,2,3,4]
flowers = [3,2,1]
print(sol.kEmptySlots(flowers, 1))

