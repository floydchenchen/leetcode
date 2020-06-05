# 169. Majority Element

# Given an array of size n, find the majority element. The majority element
# is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    # Moore voting algorithm
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 每次从序列里选择两个不相同的数字删除掉（或称为“抵消”），最后剩下一个数字或几个相同的数字，就是出现次数大于总数一半的那个
        # 分别用major和count记录major element和它出现的数量
        major, count = nums[0], 1
        for i in range(1, len(nums)):
            # 选择新的major element
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major

sol = Solution()
print(sol.majorityElement([0,2,2,1,1,2,3,2,2]))