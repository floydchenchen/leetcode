# 281. Zigzag Iterator

# Given two 1d vectors, implement an iterator to return their elements alternately.
#
# Example:
#
# Input:
# v1 = [1,2]
# v2 = [3,4,5,6]
#
# Output: [1,3,2,4,5,6]
#
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,3,2,4,5,6].
# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
#
# Clarification for the follow up question:
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you,
# replace "Zigzag" with "Cyclic". For example:
#
# Input:
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# Output: [1,4,8,2,5,9,3,6,7].

# 思路：zig zag queue
class ZigzagIterator:

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = [l for l in [v1, v2] if l]

    def next(self):
        """
        :rtype: int
        """
        l = self.q.pop(0)
        result = l.pop(0)
        if l:
            self.q.append(l)
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.q:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
