# 232. Implement Queue using Stacks

# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false

# push O(1), pop amortized O(1)
class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x):
        self.s1.append(x)

    # 每次要pop之前，先peek，然后从s2里pop
    def pop(self):
        self.peek()
        return self.s2.pop()

    # 每次peek都从s2中peek, 如果s2是空的，直接把s2填满
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()