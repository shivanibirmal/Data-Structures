# 150. Evaluate Reverse Polish Notation
# Medium
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# Example 1:
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ["+", "/", "*", "-"]
        my_stack = []

        for i in tokens:
            if i in operators:
                op2 = my_stack.pop()
                op1 = my_stack.pop()

                op_index = operators.index(i)
                if op_index == 0:
                    res = op1 + op2
                    my_stack.append(res )
                    continue
                elif op_index == 1:
                    res = int(op1/op2)
                    my_stack.append(res )
                    continue
                elif op_index == 2:
                    res = op1 * op2
                    my_stack.append(res )
                    continue
                else:
                    res = op1 - op2
                    my_stack.append(res )

                print("Push",op1, operators[op_index],op2,"=",res)

            else:
                my_stack.append(int(i))

        return my_stack.pop()

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
obj = Solution()
result = obj.evalRPN(tokens)
print("output", result)
