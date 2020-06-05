# 218. The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/description/
# https://briangordon.github.io/2014/08/the-skyline-problem.html

# 思路：每一栋房子有左右两个临界点，从左往右扫过每一个临界点，我们只需要记录每一个临界点的最高的房子的高度即可
# 如何快速找到每个临界点的最高房子的高度：每一个临界点都有用一个以房子的高度降序排序的max_heap，记录了active的所有房子
# 记录房子高度的max_heap：到达房子左临界点时，将该房子加入active max_heap；到达房子右临界点时，将房子移出active max_heap

from collections import OrderedDict
from heapq import *


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # 用OrderedDict来记录每个临界点的所有房子
        dic = {}
        for building in buildings:
            for i in range(2):
                dic[building[i]] = dic.get(building[i], []) + [building]
        dic = OrderedDict(sorted(dic.items(), key=lambda b: b[0]))

        heap, result = [], []
        for critical in dic.keys():
            for building in dic[critical]:
                # if left edge of the building, add building to active heap
                if critical == building[0]:
                    heappush(heap, (-building[2], building[0], building[1]))
                # if right edge of the building, remove building from heap
                else:
                    # the python way of remove a specific element from heap
                    heap.remove((-building[2], building[0], building[1]))
                    heapify(heap)

            # if heap is empty, then skyline is of 0 height
            if len(heap) == 0:
                result.append([critical, 0])
            else:
                height = -heap[0][0]
                # only add the highest rectangle if different than before
                if len(result) == 0 or result[-1][1] != height:
                    result.append([critical, height])
        return result


sol = Solution()
print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
