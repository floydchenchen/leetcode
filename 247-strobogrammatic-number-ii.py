# 247. Strobogrammatic Number II

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
# Input:  n = 2
# Output: ["11","69","88","96"]

# 思路：dictionary存对应关系，recursive divide and conquer
# 已知n=1 和n=2的所有结果
# 当n是奇数时，把list_1的结果分别插入到n-1的结果中
# 当n是偶数时，把list_2的结果分别插入到n-2的结果中
# Some observation to the sequence:
#
# n == 1: [0, 1, 8]
#
# n == 2: [11, 88, 69, 96]
#
# How about n == 3?
# => it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 2
#
# n == 4?
# => it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 2
#
# n == 5?
# => it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 4
#
# the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4
class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_1 = ["0", "1", "8"]
        # 注意最后的00
        list_2 = ["11","69","88","96", "00"]
        if n == 1:
            return list_1
        # 注意不要最后的00
        if n == 2:
            return list_2[:-1]
        if n % 2 == 1:
            pre_list, l = self.findStrobogrammatic(n-1), list_1
        else:
            pre_list, l = self.findStrobogrammatic(n - 2), list_2

        pre_mid = (n - 1) // 2
        return [p[:pre_mid] + c + p[pre_mid:] for c in l for p in pre_list]