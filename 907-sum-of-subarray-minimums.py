# 907. Sum of Subarray Minimums

# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

# e.g. given [3,1,2,4],
# For 3, the boudary is: | 3 | ...
# For 1, the boudray is: | 3 1 2 4 |
# For 2, the boudray is: ... | 2 4 |
# For 4, the boudary is: ... | 4 |

# The times a number n occurs in the minimums is (cur - l) * (r - cur): 这个其实是一个combination的问题
# The total sum is sum([n * (cur - l) * (r - cur) for n in array])
# # 单调递增栈 (<=)

from math import inf
class Solution:
    def sumSubarrayMins(self, A):
        result = 0
        # 单调递增栈
        stack = []
        # 左右加两个dummy，这样就能够在开始和结束的时候处理左右两个边界
        A = [-inf] + A + [-inf]
        for r in range(len(A)):
            # 如果单调递增栈里的最高一个数 > A[r]，说明r是当前递增window的一个right boundary
            while stack and A[stack[-1]] > A[r]:
                cur = stack.pop()
                result += A[cur] * (cur - stack[-1]) * (r - cur)
            stack.append(r)
        # Since the answer may be large, return the answer modulo 10^9 + 7.
        # return result % (10**9 + 7)
        return result

sol = Solution()
print(sol.sumSubarrayMins([3,1,2,4]))