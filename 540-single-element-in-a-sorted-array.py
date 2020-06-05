# 540. Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once. Find this single element that appears only once.

# Example 1:

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: [3,3,7,7,10,11,11]
# Output: 10

class Solution:
    # binary search
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            neighbor = mid + 1 if mid % 2 == 0 else mid - 1
            # ��ֹneighborԽ��
            if neighbor < len(nums) and nums[mid] == nums[neighbor]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]