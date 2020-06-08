# 460. LFU Cache

# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
# t should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie 
# (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. 
# This number is set to zero when the item is removed.

 

# Follow up:
# Could you do both operations in O(1) time complexity?

 

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       # returns 1
# cache.put(3, 3);    # evicts key 2
# cache.get(2);       # returns -1 (not found)
# cache.get(3);       # returns 3.
# cache.put(4, 4);    # evicts key 1.
# cache.get(1);       # returns -1 (not found)
# cache.get(3);       # returns 3
# cache.get(4);       # returns 4


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.size = 0
        # 将两个node连起来
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addFirst(self, node: Node) -> None:
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        self.size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def removeLast(self) -> None:
        if self.size > 0:
            node = self.tail.prev
            self.remove(node)
            return node
        return None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_dic = {}
        self.freq_dic = {}
        self.min_freq = -1

    def get(self, key: int) -> int:
        if key not in self.node_dic:
            return -1
        node = self.node_dic.get(key)
        self.update(node)
        return node.val
    
    # add new node into LFU cache, as well as double linked list
    # condition 1: if LFU cache has input key, update node value and node position in list
    # condition 2: if LFU cache does NOT have input key
    #  - sub condition 1: if LFU cache does NOT have enough space, remove the Least Frequently Used node
    #  in minimum frequency list, then add new node
    #  - sub condition 2: if LFU cache has enough space, add new node directly
    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key not in self.node_dic:
            node = Node(key, value)
            self.node_dic[key] = node
            if len(self.node_dic) > self.capacity:
                # get minimum frequency list
                minFreqList = self.freq_dic.get(self.min_freq)
                self.node_dic.pop(minFreqList.removeLast().key)
            # reset min frequency to 1 because of adding new node
            self.min_freq = 1
            # get the list with frequency 1, and then add new node into the list, as well as into LFU cache
            newList = self.freq_dic.get(node.freq, DLinkedList())
            newList.addFirst(node)
            self.freq_dic[node.freq] = newList
        else:
            node = self.node_dic.get(key)
            node.val = value
            self.update(node)
    
    def update(self, node: Node) -> None:
        oldList = self.freq_dic.get(node.freq)
        oldList.remove(node)
        # edge case
        # if current list is the last list which has lowest frequency and current node is the only node in that list
        # we need to remove the entire list and then increase min frequency value by 1
        if node.freq == self.min_freq and oldList.size == 0:
            self.min_freq += 1
        node.freq += 1
        # add current node to another list has current frequency + 1,
        # if we do not have the list with this frequency, initialize it
        newList = self.freq_dic.get(node.freq, DLinkedList())
        newList.addFirst(node)
        self.freq_dic[node.freq] = newList

cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.get(3)       # returns 3.
cache.put(4, 4)    # evicts key 1.
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4