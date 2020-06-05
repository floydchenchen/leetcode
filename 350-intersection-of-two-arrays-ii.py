# 350. Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
#
# Follow up:
#
# 1. What if the given array is already sorted? How would you optimize your algorithm?
# 2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 3. What if elements of nums2 are stored on disk, and the memory is limited such that
# you cannot load all elements into the memory at once?

# follow-up解答
# 1. If both arrays are sorted, I would use two pointers to iterate,
# which somehow resembles the merge process in merge sort.
#
# 2. use smaller array to build Counter, to optimize space
#
# 3. Divide and conquer. Repeat the process frequently: Slice nums2 to fit into memory,
# process (calculate intersections), and write partial results to memory.

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        # elements(): Return an iterator over elements repeating each as many times as its count.
        # Elements are returned in arbitrary order. If an element’s count is less than one,
        # elements() will ignore it.
        return list((c1 & c2).elements())
        # return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

print(Solution().intersect([4,9,5,9],[9,4,9,8,4]))