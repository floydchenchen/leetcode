# 381. Insert Delete GetRandom O(1) - Duplicates allowed

# Design a data structure that supports all following operations in average O(1) time.
#
# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements.
# The probability of each element returned is linearly related to the number of same value the collection contains.
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);
#
# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();

from random import choice
from collections import defaultdict


class RandomizedCollection(object):

    def __init__(self):
        self.nums, self.indices = [], defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.indices[val].add(len(self.nums) - 1)
        return len(self.indices[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.indices[val]:
            out, ins = self.indices[val].pop(), self.nums[-1]
            self.nums[out] = ins
            if self.indices[ins]:
                self.indices[ins].add(out)
                self.indices[ins].discard(len(self.nums) - 1)
            self.nums.pop()
            return True
        return False

    def getRandom(self):
        return choice(self.nums)
