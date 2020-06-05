# 143. Reorder List

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# 思路：fast and slow pointer
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # edge case
        if not head or not head.next:
            return
        # 1. find the mid
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # important: point the tail of the first half to None
        prev.next = None
        
        # 2. reverse the right half of the list
        prev, cur = slow, slow.next
        prev.next = None
        while cur:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next
        
        # 3. insert the second half to the first half
        l1, l2 = head, prev
        while l1:
            next_l1, next_l2 = l1.next, l2.next
            l1.next = l2
            if next_l1:
                l2.next = next_l1
            l1 = next_l1
            l2 = next_l2
        return head

