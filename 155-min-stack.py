# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


# class MaxStack:
#
# 	def __init__(self):
# 		self.stack, self.min_stack = [], []
#
# 	def push(self, n):
# 		self.stack.append(n)
# 		if not self.min_stack or self.min_stack[-1] <= n:
# 			self.min_stack.append(n)
# 		else:
# 			self.min_stack.append(self.min_stack[-1])
#
# 	def top(self):
# 		return self.stack[-1]
#
# 	def pop(self):
# 		self.min_stack.pop()
# 		return self.stack.pop()
#
# 	def peekMax(self):
# 		return self.min_stack[-1]

class MinStack:

    def __init__(self):
        self.stack, self.min_stack = [], []

    def push(self, n):
        self.stack.append(n)
        if not self.min_stack or self.min_stack[-1] >= n:
            self.min_stack.append(n)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()