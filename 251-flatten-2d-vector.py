# 251. Flatten 2D Vector

# Implement an iterator to flatten a 2d vector.
#
# Example:
#
# Input: 2d vector =
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# Output: [1,2,3,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,2,3,4,5,6].
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.

class Vector2D:

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row, self.col = 0, 0
        self.vec = vec2d

    def next(self):
        """
        :rtype: int
        """
        result = self.vec[self.row][self.col]
        self.col += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            self.col = 0
            self.row += 1
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
