# 128. Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 1, 200, 1, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# 注意sequence中可能有duplicate

# 思路：1. 先用set存所有distinct的元素 2. 扫一遍array，对每一个num搜num左右在set中的相邻的值(left = num - i, right = num + j)，
# 并将找到的这些相同的值从set中去掉，同时更新最大的count
class Solution(object):
    # 用set去除掉duplicate
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _set = set(nums)
        result = 0
        for num in nums:
            count = 1
            # check left and right
            left = right = num
            print("num: ", num)
            print(_set)
            while (left - 1) in _set:
                count += 1
                left -= 1
                _set.remove(left)
                print(_set)
            while (right + 1) in _set:
                count += 1
                right += 1
                _set.remove(right)
                print(_set)
            result = max(result, count)
        return result
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))