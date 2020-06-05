# 142. Linked List Cycle II

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Note: Do not modify the linked list.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# When fast and slow meet at point p, the length they have run are 'a+2b+c' and 'a+b'.
# Since the fast is 2 times faster than the slow. So a+2b+c == 2(a+b), then we get 'a==c'.
# So when another slow2 pointer run from head to 'q', at the same time, previous slow pointer will run from 'p' to 'q', so they meet at the pointer 'q' together.
# see image at: https://farm6.staticflickr.com/5758/22715587283_bdb4ba8434.jpg

class Solution(object):
	# floyd's loop algorithm, iterative
	# distance from head to loop node is A, and loop length this C
	# slow travels: A + B, fast travels: 2A + 2B, and A + B + C = 2A + 2B, so C = A + B. thus slows travels C(full length)
	# slow pointer traveled exactly full cycle when it meets fast pointer
    def detectCycle(self, head):
		if not head:
			return None
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				while slow != head:
					head = head.next
					slow = slow.next
				return slow
		return None

