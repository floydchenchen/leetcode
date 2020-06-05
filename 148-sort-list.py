# 148. Sort List

# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路：merge sort, fast and slow pointer
class Solution:
    
    def find_middle_node(self, head):
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow
    
    # merge in-place without dummy node        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        # 首先让l第一个node小于r第一个node
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else: # 需要进行merge
                next_l = pre.next
                pre.next = r
                next_r = r.next
                r.next = next_l
                r = next_r
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head
    
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        mid = self.find_middle_node(head)
        r_head = mid.next
        mid.next = None
        l = self.sortList(head)
        r = self.sortList(r_head)
        
        return self.merge(l, r)