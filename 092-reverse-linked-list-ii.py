# 92. Reverse Linked List II

# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # 先找到新的pre
        for _ in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        # first, second, third = None, pre.next, pre.next.next
        # third = pre.next.next could be None, then third = third.next in the for loop could lead to an error
        first, second = None, pre.next
        for _ in range(n - m + 1):
            third = second.next
            second.next = first
            first = second
            second = third

        # connect reverse_end to right_start
        pre.next.next = second
        # connect left_end to reverse_start
        pre.next = first

        return dummy.next


