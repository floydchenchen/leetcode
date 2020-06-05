# coding: gbk
# 416. Partition Equal Subset Sum
# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.
 

# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.

# ������ת���ɣ��Ƿ��nums�������ֱ�Ϊnums[i]����Ʒװ��һ������Ϊ(sum/2)�������Ƿ����һ��װ����ʹ�ñ����պ���װװ��
# dp[i][j]: if the subset from the first i items can reach a sum of j.
# initialization: dp[i][0] = 0
# ����ѡ��װ�뱳�����߲�װ�뱳��
# transition: dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]])
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # edge cases
        _sum = sum(nums)
        if _sum & 1:
            return False
        _sum //= 2
        
        # initilaize dp table
        n = len(nums)
        dp = [([True] + [False] * _sum) for _ in range(n+1)]
        for i in range(1, n + 1):
            for j in range(1, _sum + 1):
                # ������������
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]])
        return dp[n][_sum]

sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))
