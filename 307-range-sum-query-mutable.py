# 307. Range Sum Query - Mutable

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8

class SegmentTree:
	def __init__(self, start, end, sum):
		self.start, self.end, self.sum = start, end, sum
		self.left, self.right = None, None

	def build(self, nums, start, end):
		# exit
		if start > end:
			return None

		root = SegmentTree(start, end, nums[start])
		if start == end:
			return root

		mid = (start + end) // 2
		root.left = self.build(nums, start, mid)
		root.right = self.build(nums, mid + 1, end)

		# update sum
		root.sum = root.left.sum + root.right.sum

		return root

	def query(self, root, start, end):
		# exit: query区间与树的区间不相交
		if root.start > end or root.end < start:
			return 0

		# query区间包含树的区间
		if start <= root.start and root.end <= end:
			return root.sum

		# query区间与树的区间相交
		return self.query(root.left, start, end) + self.query(root.right, start, end)

	def modify(self, root, index, value):
		# exit
		if not root:
			return

		# found the node and modify it
		if root.start == root.end:
			root.sum = value
			return

		if root.left.end >= index:
			self.modify(root.left, index, value)
		else:
			self.modify(root.right, index, value)

		# don't forget to update root.sum!
		root.sum = root.left.sum + root.right.sum

class NumArray:

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.seg = SegmentTree(0, len(nums), 0)
		self.tree = self.seg.build(nums, 0, len(nums)-1)

	def update(self, i, val):
		"""
		:type i: int
		:type val: int
		:rtype: void
		"""
		self.seg.modify(self.tree, i, val)

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		return self.seg.query(self.tree, i, j)
