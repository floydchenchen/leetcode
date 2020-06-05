# 206. Reverse Linked List
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# iterative
	def reverseList(self, head):
		"""
        :type head: ListNode
        :rtype: ListNode
        """
		if not head:
			return head

		pre, cur = None, head
		while head:
			head = head.next
			cur.next = pre
			pre = cur
			cur = head
		return pre

	def reverseListRecursive(self, head):

		def helper(pre, cur):
			# exit
			if not cur:
				return pre

			_next = cur.next
			cur.next = pre
			pre = cur
			cur = _next
			return helper(pre, cur)

		return helper(None, head)
