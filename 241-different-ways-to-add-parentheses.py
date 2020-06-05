# 241. Different Ways to Add Parentheses

# Given a string of numbers and operators, return all possible results from computing all the different possible
# ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10

class Solution:
    # recursive divide and conquer
    def diffWaysToCompute(self, input):

        def helper(m, n, op):
            if op == "+":
                return m + n
            elif op == "-":
                return m - n
            else:
                return m * n

        # exit，只有数字，没有operators
        if input.isdigit():
            return [int(input)]
        result = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for j in res1:
                    for k in res2:
                        result.append(helper(j, k, input[i]))
        return result

print(Solution().diffWaysToCompute("2*3+4"))