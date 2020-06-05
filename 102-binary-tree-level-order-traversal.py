# 102. Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# BFS
	def levelOrder(self, root):
		q = []
		result = []
		if not root:
			return result

		q.append(root)

		while q:
			level_list = []
			level_size = len(q)
			# 不能直接用 range(len(q))，因为len(q)会变！
			for _ in range(level_size):
				node = q.pop(0)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
				level_list.append(node.val)
			result.append(level_list)

		return result

	# DFS
	def levelOrder1(self, root):
		def dfs(root, height, result):
			if not root:
				return
			# new level
			if height >= len(result):
				result.append([])
			result[height].append(root.val)
			dfs(root.left, height + 1, result)
			dfs(root.right, height + 1, result)

		result = []
		dfs(root, 0, result)
		return result

