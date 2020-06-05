# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
# also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# 思路： product和sum做法不同，不像sum一样两个pointer从右到左扫过，而是每一位都可能过很多遍（下面的例子）
# 所以注意在每次操作之后 product[tempPos] %= 10
# 1. 先建一个len(num1) + len(num2) 大的product list
# 2. 两个数从后往前，两个for-loop做乘法（如下图）
# 3. 为了避免2*3=6而不是06这种情况，将leading zeros去掉

#   _ _ _ 1 2 3
# x _ _ _ 4 5 6
# -------------
#         7 3 8
#       6 1 5
#     4 9 2
# -------------
#     5 6 0 8 8

class Solution:
    def multiply(self, num1, num2):
        # 1. 先建一个len(num1) + len(num2) 大的product list
        product = [0] * (len(num1) + len(num2))

        # 2. 两个数从后往前，两个for-loop做乘法
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product[j + i + 1] += int(num1[i]) * int(num2[j])
                product[j + i] += product[j + i + 1] // 10
                product[j + i + 1] %= 10
                # print(product)

        # 3. 为了避免2*3=6而不是06这种情况，将leading zeros去掉
        start_index = 0
        while start_index < len(product) - 1 and product[start_index] == 0:
            start_index += 1

        return ''.join(map(str, product[start_index:]))

print(Solution().multiply("2","3"))