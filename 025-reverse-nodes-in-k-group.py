# 25. Reverse Nodes in k-Group

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# 就是要反转前k个Node

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # edge case
        if not head or k < 2:
            return head

        # find the next_head, and put the result head in dummy.next
        # also check if k is too large
        next_head = head
        dummy = ListNode(0)
        for i in range(k - 1):
            next_head = next_head.next
            # if k is too large
            if not next_head:
                return head
        dummy.next = next_head

        cur = head
        while next_head:
            tail = cur
            pre = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                _next = cur.next
                cur.next = pre
                pre = cur
                cur = _next
            # 如果not next_head, tail.next指向cur
            tail.next = next_head or cur

        return dummy.next
