# 366. Find Leaves of Binary Tree

# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves,
# repeat until the tree is empty.
#
#
#
# Example:
#
# Input: [1,2,3,4,5]
#
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# Output: [[4,5,3],[2],[1]]
#
#
# Explanation:
#
# 1. Removing the leaves [4,5,3] would result in this tree:
#
#           1
#          /
#         2
#
#
# 2. Now removing the leaf [2] would result in this tree:
#
#           1
#
#
# 3. Now removing the leaf [1] would result in the empty tree:
#
#           []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    # recursive divide and conquer + dictionary
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 和depth是反的，leaf时是order为0，root的order是max(left, right) + 1
        def order(root, dic):
            if not root:
                return 0
            left, right = order(root.left, dic), order(root.right, dic)
            level = max(left, right) + 1
            dic[level].append(root.val)
            return level

        dic, result = defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            result.append(list(dic[i]))
        return result


