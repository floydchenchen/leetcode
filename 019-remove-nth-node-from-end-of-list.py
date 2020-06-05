# 19. Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        # 先将fast右移n位
        for _ in range(n):
            fast = fast.next
        # 注意check n是否长于linked list，如果是的话，return head.next
        if not fast:
            return head.next

        # 通过fast到达末位，slow到达需要移除的前一个node
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 移除目标node
        slow.next = slow.next.next
        return head
