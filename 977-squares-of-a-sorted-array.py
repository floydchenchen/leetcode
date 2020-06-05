# 977. Squares of a Sorted Array

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution:
    # two pointers, following negative and non-negative numbers
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                result.insert(0, left * left)
                l += 1
            else:
                result.insert(0, right * right)
                r -= 1
        return result