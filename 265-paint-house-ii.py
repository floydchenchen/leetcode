# 265. Paint House II

# There are a row of n houses, each house can be painted with one of the k colors.
# The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix.
# For example, costs[0][0] is the cost of painting house 0 with color 0;
# costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
#              Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
# Follow up:
# Could you solve it in O(nk) runtime?


# 思路跟256基本一样，就是把颜色变成了k种，这时我们用两个pointer min_1 < min_2；当min_1的的颜色和上一个房子颜色相同时，
# 我们更新dp[i][j为]min_2，否则更新为min_1
class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        for i in range(1, len(costs)):
            min1 = min(costs[i-1])
            min1_index = costs[i-1].index(min1)
            min2 = min(costs[i-1][:min1_index] + costs[i-1][min1_index+1:])
            for j in range(len(costs[i])):
                if j == min1_index:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])

