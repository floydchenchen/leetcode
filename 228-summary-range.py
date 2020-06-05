# 228. Summary Ranges

# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) == 1:
            result.append(str(nums[0]))
            return result
        i = 0
        while i < len(nums):
            temp = nums[i]
            while i + 1 < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            if temp != nums[i]:
                result.append(str(temp) + "->" + str(nums[i]))
            else:
                result.append(str(temp))
            i += 1
        return result
