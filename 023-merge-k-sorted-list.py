# 23. Merge k Sorted Lists

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

from heapq import *
class Solution:

	def mergeKLists(self, lists):
		"""
        :type lists: List[ListNode]
        :rtype: ListNode
        """
		dummy = cur = ListNode(0)
		# 这里必须要index，因为enmuerate(lists)之后，要用index去在heapify的时候作比较
		heap = [(node.val, index, node) for index, node in enumerate(lists) if node]
		heapify(heap)
		while heap:
			val, index, node = heappop(heap)
			cur.next = node
			cur = cur.next
			if node.next:
				heappush(heap, (node.next.val, index, node.next))

		return dummy.next

sol = Solution()

a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = ListNode(2)
c.next = ListNode(6)

def list(node):
	result = []
	while node:
		result.append(node.val)
		node = node.next
	return result

print(list(sol.mergeKLists([a,b,c])))