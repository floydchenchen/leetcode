# 170. Two Sum III - Data structure design

# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# Example 1:
#
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# Example 2:
#
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false

from collections import defaultdict
class TwoSum:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.dic = defaultdict(int)

	# O(1) add
	def add(self, number):
		"""
		Add the number to an internal data structure..
		:type number: int
		:rtype: void
		"""
		self.dic[number] += 1

	# O(n) find
	def find(self, value):
		"""
		Find if there exists any pair of numbers which sum is equal to the value.
		:type value: int
		:rtype: bool
		"""
		for num in self.dic:
			if value - num in self.dic and (value - num != num or self.dic[num] > 1):
				return True
		return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)