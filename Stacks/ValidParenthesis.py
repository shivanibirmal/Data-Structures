# 20. Valid Parentheses
# Easy

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '[', '{']
        closed_brackets = [')', ']', '}']
        str_len = len(s)
        my_stack = []

        if str_len == 0:
            return True

        if str_len % 2 != 0:
            return False

        for i in s:
            if i in open_brackets:
                my_stack.append(i)

            elif my_stack and open_brackets.index(my_stack[-1]) == closed_brackets.index(i):
                    my_stack.pop()
            else:
                return False

        return my_stack == []

s = "{[]}{[]}"
obj = Solution()
result = obj.isValid(s)
print("Is",s,"a valid string of parenthesis?", result)

# Method of solving

# for every character in the string, if it is an opening bracket, push it on the Stack
# If it is a closing bracket, then check the top of the stack. If the top holds the opening bracket corresponding
# to the current element, then pop it.
# if after all iterations, the stack is not empty, then it is not a valid sequence
