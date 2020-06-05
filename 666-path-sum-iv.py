# 666. Path Sum IV

# If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
#
# For each integer in this list:
# The hundreds digit represents the depth D of this node, 1 <= D <= 4.
# The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8.
# The position is the same as that in a full binary tree.
# The units digit represents the value V of this node, 0 <= V <= 9.
# Given a list of ascending three-digits integers representing a binary with the depth smaller than 5.
# You need to return the sum of all paths from the root towards the leaves.
#
# Example 1:
# Input: [113, 215, 221]
# Output: 12
# Explanation:
# The tree that the list represents is:
#     3
#    / \
#   5   1
#
# The path sum is (3 + 5) + (3 + 1) = 12.
# Example 2:
# Input: [113, 221]
# Output: 4
# Explanation:
# The tree that the list represents is:
#     3
#      \
#       1
#
# The path sum is (3 + 1) = 4.

class Solution:
    # to do normal tree traversal, we build a tree
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # store the tree in a 2D matrix
        result = 0
        tree = [[None] * (8 + 1) for _ in range(4 + 1)]
        # build the tree
        for num in nums:
            lvl, pos, val = num // 100, (num // 10) % 10, num % 10
            tree[lvl][pos] = val
            # do pre-sum
            if lvl > 1:
                parent = tree[lvl - 1][(pos + 1) // 2]
                tree[lvl][pos] += parent
        # find the path
        for num in nums:
            lvl, pos, val = num // 100, (num // 10) % 10, num % 10
            # check if this node is a leaf
            if lvl == 4 or (not tree[lvl + 1][pos * 2 - 1] and not tree[lvl + 1][pos * 2]):
                result += tree[lvl][pos]
        return result


sol = Solution()
# print(sol.pathSum([111,217,221,315,415]))
print(sol.pathSum([113,215,221]))
