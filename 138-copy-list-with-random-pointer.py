# 138. Copy List with Random Pointer
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
#
# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 这个题主要是需要解决random pointer的问题，在建node的时候，不能同时建好pointer
# 用map解决pointer的问题，将时间复杂度从O(n^2)降低到O(2n)
# (two pass: one pass for creating dictionary, one pass for assigning pointers)
# 直接用node来做map的key
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        m = n = head
        # first pass, creating dictionary using node as the key
        while m:
            dic[m] = Node(m.val)
            m = m.next

        # second pass, assigning random and next pointers
        # 一定要写成dic.get来避免null
        while n:
            dic[n].random = dic.get(n.random)
            dic[n].next = dic.get(n.next)
            n = n.next
        return dic.get(head)
