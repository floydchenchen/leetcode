# 31. Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        # 1. 找从右往左第一个正序, i: first smaller (nums[i] < nums[i+1])
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1

        # 2. 如果完全是逆序，那么让这个数变成正序[3,2,1 -> 1,2,3]，结束
        if i == -1:
            # 不能用nums = nums[::-1]
            nums = nums.reverse()
            return

        # 3. 找i(first smaller)右边的从右往左第一个比它大的数: j
        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1

        # 4. 交换i和j
        nums[i], nums[j] = nums[j], nums[i]

        # 5. 把firstSmaller之后的数reverse order(或者sort一下)
        nums[i+1:] = sorted(nums[i+1:])




sol = Solution()
nums = [1,2,3]
sol.nextPermutation(nums)
print(nums)