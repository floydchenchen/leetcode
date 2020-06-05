# 378. Kth Smallest Element in a Sorted Matrix

# Given a n x n matrix where each of the rows and columns are sorted in ascending order,
# find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.

# binary search in a sorted 2d array
# 稍微不同的是，根据value找index
import bisect

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        start, end = matrix[0][0], matrix[-1][-1]
        while start <= end:
            mid = (start + end) // 2
            # 对value的binary search
            # bisect.bisect_right(row, mid) 返回row这个list中的第一个大于mid的插入位置，也就是这个row说有几个小于等于mid的元素
            # bisect.bisect_right(row, mid) for row in matrix: 返回matrix中所有row的结果组成的一个list
            # 这一行太精髓了！找有多少个小于mid value的值
            # 可以变成bisect_right
            if sum(bisect.bisect_left(row, mid) for row in matrix) < k:
                start = mid + 1
            else:
                end = mid - 1
        # 可以变成start
        return end


sol = Solution()
print(sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
