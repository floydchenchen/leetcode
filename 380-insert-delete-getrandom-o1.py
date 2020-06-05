# 380. Insert Delete GetRandom O(1)

# Design a data structure that supports all following operations in average O(1) time.
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements.
# Each element must have the same probability of being returned.
# Example:
#
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

# 直接用set的话，我们没法保证从set里获取一个random的数，所以必须要有index的结构(list)
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.indices = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            self.nums.append(val)
            # the last index of nums
            self.indices[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            # 把最后一个放到要remove的位置，再pop最后一个
            index = self.indices[val]
            last = self.nums[-1]
            self.nums[index] = last
            self.nums.pop()
            self.indices[last] = index
            del self.indices[val]
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()