"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
      # Each element in the stack will be a tuple, (x, y). x is value, y is min value at the time.
      self.stack = []

    def push(self, x: int) -> None:
      if self.stack:
        self.stack.append((x, min(x, self.stack[-1][1])))
      else:
        self.stack.append((x, x))

    def pop(self) -> None:
      popped = self.stack[-1][0]
      self.stack = self.stack[:-1]
      return popped

    def top(self) -> int:
      return self.stack[-1][0]

    def getMin(self) -> int:
      return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()