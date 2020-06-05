# 160. Intersection of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 这个方法不是特别高效
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        # 有点类似slow and fast pointers，我们只需要在一个指针到达末尾后，让该指针重新指向head
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA.next else headA
            pB = pB.next if pB.next else headB
        return pA

    # 更高效率的方法：让两个head从距离交汇点相同地方的位置开始
    def getIntersectionNode1(self, headA, headB):
        def get_len(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        lenA, lenB = get_len(headA), get_len(headB)

        # move headA and headB to the same start point
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        # find the intersection
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        return headA
