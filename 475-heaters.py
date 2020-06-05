# 475. Heaters

# Winter is coming! Your first job during the contest is to design a standard heater
# with fixed warm radius to warm all the houses.
#
# Now, you are given positions of houses and heaters on a horizontal line,
# find out minimum radius of heaters so that all houses could be covered by those heaters.
#
# So, your input will be the positions of houses and heaters seperately,
# and your expected output will be the minimum radius standard of heaters.
#
# Note:
# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.
#
# Example 1:
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard,
# then all the houses can be warmed.
#
# Example 2:
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard,
# then all the houses can be warmed.

# 0 1 2 3
# 0 1 2 3 4

# 给出房子和炉子的位置，找出能覆盖所有房子的炉子的最小半径
# binary search类型2：查找第一个不小于目标值的数

# time: O(nlgn)
from math import inf
import bisect


class Solution:
    # 思路1：把house放到两个heater之间，再来作比较，找出离house最近的heater距离
    def findRadius(self, houses, heaters):
        # two dummy heaters at the beginning and the end
        heaters = [-inf] + sorted(heaters) + [inf]
        result, i = 0, 0
        for house in sorted(houses):
            # search to put house between heaters
            while house > heaters[i + 1]:
                i += 1
            distance = min(house - heaters[i], heaters[i + 1] - house)
            result = max(result, distance)
        return result

    # 思路2: binary search
    def findRadius1(self, houses, heaters):
        # two dummy heaters at the beginning and the end
        heaters = [-inf] + sorted(heaters) + [inf]
        print("heaters", heaters)
        result = 0
        for house in houses:
            # 将house插入到两个heaters之间
            # index of the right heater, 查到最后一个小于目标值的数
            index = bisect.bisect_left(heaters, house)
            left_heater, right_heater = heaters[index - 1], heaters[index]
            result = max(result, min(house - left_heater, right_heater - house))
        return result

sol = Solution()
print(sol.findRadius1([1,2,3,4],[1,4]))