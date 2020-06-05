# 572. Subtree of Another Tree
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values
# with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# 方法1：isSameTree helper function
	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		def isSameTree(s, t):
			if not s and not t:
				return True
			if not s or not t:
				return False
			return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

		if not s:
			return False
		return isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

	# 方法2：serialize two trees
	def isSubtree1(self, s, t):
		def convert(p):
			return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "x"

		return convert(t) in convert(s)

print(Solution.isSubtree1())