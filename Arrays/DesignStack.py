# 155. Min Stack
# Easy

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
# Constraints:
#
# Methods pop, top and getMin operations will always be called on non-empty stacks.

# DO NOT USE MIN() FOR FINDING MINIMUM ELEMENT OF STACK

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack :
            self.stack.append((x,x))
        else:
            current_minimum = self.stack[-1][1]
            self.stack.append((x, min(x, current_minimum)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
