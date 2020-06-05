# 88. Merge Sorted Array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space
# (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#w
# Output: [1,2,2,3,5,6]

class Solution:
    # three pointer: i, j, k 分别
    # 为什么从后往前加：这样不会覆盖nums1中的小的元素
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # 如果i >= 0，不用管，因为这些元素本来就在合适的位置上了
        # 如果 j >= 0，说明此时nums2还有一些比nums1更小的元素，要放到nums1的最前面
        # 例如 nums1 = [4,5,6,0,0,0], nums2 = [1,2,3]
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1