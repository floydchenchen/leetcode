# 385. Mini Parser

# Given a nested list of integers represented as a string, implement a parser to deserialize it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Note: You may assume that the string is well-formed:
#
# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].
# Example 1:
#
# Given s = "324",
#
# You should return a NestedInteger object which contains a single integer 324.
# Example 2:
#
# Given s = "[123,[456,[789]]]",
#
# Return a NestedInteger object containing a nested list with 2 elements:
#
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:

    # recursive solution
    def deserialize(self, s):
        def nestedInteger():
            num = ''
            while s[-1] in '1234567890-':
                num += s.pop()
            if num:
                return NestedInteger(int(num))
            s.pop()
            lst = NestedInteger()
            while s[-1] != ']':
                lst.add(nestedInteger())
                if s[-1] == ',':
                    s.pop()
            s.pop()
            return lst

        s = list(' ' + s[::-1])
        return nestedInteger()

    # iterative solution
    def deserialize1(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        dummy = NestedInteger()
        stack, i = [dummy], 0

        while i < len(s):
            if s[i] == '[':
                n = NestedInteger()
                stack[-1].add(n)
                stack.append(n)
                i += 1
            elif s[i] == ']':
                stack.pop()
                i += 1
            elif s[i] == ',':
                i += 1
            else:
                j = i
                while j < len(s) and ('0' <= s[j] <= '9' or s[j] == '-'):
                    j += 1
                stack[-1].add(int(s[i:j]))
                i = j

        return stack[0].getList()[0]




