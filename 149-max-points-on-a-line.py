# 149. Max Points on a Line

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Example 1:
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o
# +------------->
# 0  1  2  3  4
# Example 2:
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# 思路：对于每个点，遍历其之后的点，并建立一个map<slope, count>.
# 这个slope不一定要用除法的形式表示，可以把dx/dy用字符串的形式表示。
# 当然，在转化成字符串之前，需要把dx和dy用最大公约数处理一下。

from collections import defaultdict
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # "辗转相除法"求最大公约数
        def get_gcd(a, b):
            if b == 0:
                return a
            return get_gcd(b, a % b)

        n = len(points)
        _max = 0
        for i in range(n):
            dic = defaultdict(int)
            local_max, overlap = 0, 0

            # 只要看后面的点。如果这个点和之前的点共线，肯定已经check过了
            for j in range(i + 1, n):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y

                if dx == 0 and dy == 0:
                    # overlap表示和reference重合的点数（不含reference自己）
                    overlap += 1
                    continue

                # 如果其中一个是0，gcd就是那个非零的数。
                gcd = get_gcd(dx, dy)
                if gcd:
                    dx //= gcd
                    dy //= gcd

                # 把key处理成string
                key = str(dx) + "/" + str(dy)
                dic[key] += 1

                # local_max表示非重合的最大共线点数（不含reference自己）
                local_max = max(local_max, dic[key])
            # 这个1表示reference自己
            _max = max(_max, local_max + overlap + 1)
        return _max

sol = Solution()
print(sol.maxPoints([Point(), Point()]))


