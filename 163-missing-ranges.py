# 163. Missing Ranges
# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper],
# return its missing ranges.
#
# Example:
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        # 在nums最后加一个dummy，好处理最后的upper边界
        nums.append(upper + 1)
        pre = lower - 1
        for num in nums:
            if num == pre + 2:
                result.append(str(num - 1))
            elif num > pre + 2:
                result.append(str(pre + 1) + "->" + str(num - 1))
            pre = num
        return result

print(Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))