# 4. Median of Two Sorted Arrays

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution:
	# 解法1: quick find, general find kth smallest element from two sorted arrays
	def findMedianSortedArrays(self, A, B):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		def kth_smallest(A, B, k):
			# always keep A shorter
			if len(A) > len(B):
				A, B = B, A
			# exit
			if not A:
				return B[k]
			# edge case
			if k == len(A) + len(B) - 1:
				return max(A[-1], B[-1])

			# 最重要的步骤之一，binary search让两个list从两边同时缩小 (k // 2) 或者 len(A) (如果len(A)更小的话)的范围
			i = min(len(A) - 1, k // 2)
			j = k - i

			if A[i] > B[j]:
				return kth_smallest(A[:i], B[j:], i)
			else:
				return kth_smallest(A[i:], B[:j], j)

		l = len(A) + len(B)

		if l % 2 == 1:
			return kth_smallest(A, B, l // 2)
		else:
			return (kth_smallest(A, B, l // 2 - 1) + kth_smallest(A, B, l // 2)) / 2

sol = Solution()
print(sol.findMedianSortedArrays([1,3,5,6,8,20,25], [4,5,6,7,8,9,10,11]))