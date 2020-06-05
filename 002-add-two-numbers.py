# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# 从右往左加，输出一个linked list
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		# 考虑进位的问题
		cur_sum = 0
		node = ListNode(-1)
		# 需要dummy来储存指向linkedlist头部的指针
		dummy = node
		while l1 or l2:
			if l1:
				cur_sum += l1.val
				l1 = l1.next
			if l2:
				cur_sum += l2.val
				l2 = l2.next
			node.next = ListNode(cur_sum % 10)
			node = node.next
			# there might be a carry
			cur_sum //= 10

		# 别忘了最后可能还剩下一个carry
		if cur_sum == 1:
			node.next = ListNode(1)
		return dummy.next



