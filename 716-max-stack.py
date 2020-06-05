# 716. Max Stack

# Design a max stack that supports push, pop, top, peekMax and popMax.
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it.
# If you find more than one maximum elements, only remove the top-most one.
# Example 1:
# MaxStack stack = new MaxStack();
# stack.push(5);
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5

from heapq import *
class MaxStack:

    def __init__(self):
        self.stack = []        # stack
        self.heap = []        # heap
        self.stack_del = set()    # id of items deleted in stack but not heap
        self.heap_del = set()    # id of items deleted in heap but not stack
        self.id = 0

    # push both to stack and max heap
    def push(self, x):
        self.stack.append((self.id, x))
        heappush(self.heap, (-x, -self.id))
        self.id += 1

    # pop from stack, added to stack_del
    def pop(self):
        x = self.top()
        self.stack_del.add(self.stack.pop()[0])
        return x

    def top(self):
        while self.stack[-1][0] in self.heap_del:
            self.heap_del.remove(self.stack[-1][0])
            self.stack.pop()
        return self.stack[-1][1]

    def peekMax(self):
        while -self.heap[0][1] in self.stack_del:
            self.stack_del.remove(-self.heap[0][1])
            heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self):
        x = self.peekMax()
        _, nid = heappop(self.heap)
        self.heap_del.add(-nid)
        return x


# Your MaxStack object will be instantiated and called as such:
stack = MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
stack.top()
stack.popMax()
stack.top()
stack.peekMax()
stack.pop()
stack.top()