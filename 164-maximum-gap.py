# 164. Maximum Gap

# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Return 0 if the array contains less than 2 elements.
#
# Example 1:
#
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#              (3,6) or (6,9) has the maximum difference 3.
# Example 2:
#
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.

# 找到一个unsorted array，在它的sorted form时，相邻两个元素的最大差值

# 思路：bucket sort, bucket[i]中存i，将问题转化为求bucket中相邻元素的最大distance
import math
class Solution:
    def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = (b-a)//(len(num)-1)
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in num:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        print(bucket)
        # filter out Nones
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))

print(Solution().maximumGap([3,6,9,1]))