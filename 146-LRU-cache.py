# 146. LRU Cache

# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# 数据结构：doubly linked list (O(1)快速插入、删除node) + map（O(1)快速查询node）
# 同时维护两个数据结构

class LRUCache:

	class Node:
		def __init__(self, key: int, value: int):
			self.prev, self.next = None, None
			self.key = key # 方便map的查询
			self.value = value


	def __init__(self, capacity: int):
		self.capacity = capacity
		self.dic = {}

		# 因为要改变linkedlist的结构：删除head node，插入到tail，所以需要dummy node
		self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
		# 将两个node连起来
		self.head.next = self.tail
		self.tail.prev = self.head

	# 每一次get，都将get的Node移到doubly linkedlist最后
	def get(self, key: int) -> int:
		if key not in self.dic:
			return -1
		# remove current node
		current = self.dic[key]
		current.prev.next = current.next
		current.next.prev = current.prev

		# move current to tail
		self.move_to_tail(current)
		return current.value

	# 每次put，都先判断是否超过容量，如果是的话从dic和list中移除头部node，再将新node插入尾部
	def put(self, key: int, value: int) -> None:
		# if key already in dic, modify and return
		if self.get(key) != -1:
			self.dic[key].value = value
			return

		# check dic's size, remove the first node if dic is full
		if len(self.dic) == self.capacity:
			self.dic.pop(self.head.next.key)
			self.head.next = self.head.next.next
			self.head.next.prev = self.head

		# put new node to map, and move it to the tail of the linkedlist
		newNode = self.Node(key, value)
		self.dic[key] = newNode
		self.move_to_tail(newNode)

	# helper function
	def move_to_tail(self, node):
		node.prev = self.tail.prev
		node.next = self.tail
		self.tail.prev = node
		node.prev.next = node