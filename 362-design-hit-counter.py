# 362. Design Hit Counter

# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume
# that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing).
# You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
#
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);

# design 1: queue.
# O(1) hit, O(n) getHits, O(hit_count) space
# Poor scalability of the solution since we store all timestamps.
class HitCounter:

    def __init__(self):
        self.counter = []

    def hit(self, timestamp):
        self.counter.append(timestamp)

    def getHits(self, timestamp):
        while self.counter and timestamp - self.counter[0] >= 300:
            self.counter.pop(0)
        return len(self.counter)


# design 2: dictionary
# O(1) hit, O(n) getHits
# At least in the dictionary solution, same timestamps will not be repeated. But the dictionary can grow unbounded.
from collections import defaultdict


class HitCounter1:
    def __init__(self):
        self.counter = defaultdict(int)

    def hit(self, timestamp):
        self.counter[timestamp] += 1

    def getHits(self, timestamp):
        count = 0
        # 外面套一个list()，去避免dictionary change size during iteration的error
        for key in list(self.counter.keys()):
            if timestamp - key < 300:
                count += self.counter[key]
            else:
                del self.counter[key]
        return count


# design 3: optimized and scalable solution with circular array
# O(1) hit, O(300) getHits, constant space O(300)
# This solution will scale perfectly!
class HitCounter2:
    def __init__(self):
        self.counter = [[i + 1, 0] for i in range(300)]

    def hit(self, timestamp):
        index = (timestamp - 1) % 300
        if self.counter[index][0] == timestamp:
            self.counter[index][1] += 1
        else:
            self.counter[index][0] = timestamp
            self.counter[index][1] = 1

    def getHits(self, timestamp):
        count = 0
        for (time, time_count) in self.counter:
            if timestamp - time < 300:
                count += time_count
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
