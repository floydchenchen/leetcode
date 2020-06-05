# 83. Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # iterative solution
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            pre, cur = head, head.next
            while cur:
                if pre.val == cur.val:
                    pre.next = cur.next
                else:
                    pre = pre.next
                cur= cur.next
        return head

    # recursive solution
    def deleteDuplicates1(self, head):
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates1(head.next)
        return head.next if head.val == head.next.val else head
