# 346. Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Example:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = []
        self.size = size
        self.count = 0
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.count += 1
        self.sum += val
        self.q.append(val)
        if self.count > self.size:
            self.sum -= self.q.pop(0)
            self.count -= 1
        return self.sum / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
