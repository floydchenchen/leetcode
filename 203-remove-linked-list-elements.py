# 203. Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # check head first, head有可能有连续出现ListNode(val)
        if head:
            while head and head.val == val:
                head = head.next

        # check other nodes
        if head:
            pre, cur = head, head.next
            while cur:
                if cur.val == val:
                    pre.next = cur.next
                else:
                    pre = pre.next
                cur = cur.next

        return head
