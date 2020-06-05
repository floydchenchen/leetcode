# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
#
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


# 思路：To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references.
# Instead of thinking about in what order I change them, I just change all three at once.
class Solution:
	def swapPairs(self, head):
		if not head:
			return head
		dummy, a, b = ListNode(-1), head, head.next
		pre = dummy
		pre.next = a
		while pre.next and pre.next.next:
			a, b = pre.next, pre.next.next
			pre.next, a.next, b.next = b, b.next, a
			pre = a
		return dummy.next


