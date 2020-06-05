# 86. Partition List

# Given a linked list and a value x, partition it such that
# all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # make two list and then combine them
        dummy1 = end1 = ListNode(0)
        dummy2 = end2 = ListNode(0)

        while head:
            if head.val < x:
                end1.next = head
                end1 = end1.next
            else:
                end2.next = head
                end2 = end2.next
            head = head.next
        end2.next = None
        end1.next = dummy2.next
        return dummy1.next