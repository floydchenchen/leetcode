# 234. Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 典型的slow fast two pointers
    # 1. 通过slow fast找到中点
    # 2. reverse first half
    # 3. compare
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        rev = None

        # 通过slow fast找到中点, reverse first half
        while fast and fast.next:
            fast = fast.next.next
            # 注意学习这种python的方式！
            slow.next, rev, slow = rev, slow, slow.next
        # 处理odd length的linked list
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev



