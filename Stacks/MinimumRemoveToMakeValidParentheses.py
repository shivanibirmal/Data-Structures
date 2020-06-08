# 1249. Minimum Remove to Make Valid Parentheses
# Medium

# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.


from typing import List

class Solution:
    def minRemoveToMakeValid_Method1(self, s: str) -> str:

        brackets = ['(',')']
        bracket_stack = []
        index_stack = []
        str_len = len(s)

        for i in range(str_len):
            if s[i] in brackets:

                if s[i] == brackets[0]:
                    bracket_stack.append(s[i])
                    index_stack.append(i)
                elif bracket_stack:
                    bracket_stack.pop()
                    index_stack.pop()
                else:
                    index_stack.append(i)

        s = list(s)

        if index_stack != []:
            index_stack.reverse()
            for i in index_stack:
                s.pop(i)
        return "".join(s)

    def minRemoveToMakeValid_Method2(self, s: str) -> str:

        brackets = ['(',')']
        my_stack = []
        str_list = list(s)

        if brackets[0] not in s and brackets[1] not in s:
            return s

        for i in s:
            if i in brackets:
                if i == brackets[0]:
                    my_stack.append(i)
                elif my_stack:
                    my_stack.pop()
                else:
                    str_list.pop(str_list.index(i))

        if my_stack != []:
            str_list.reverse()
            while my_stack != []:
                index = str_list.index(my_stack.pop())
                str_list.pop(index)
            str_list.reverse()

        return "".join(str_list)

s = "lee(t(c)o)de)"
obj = Solution()
result = obj.minRemoveToMakeValid_Method1(s)
print("output", result)

result = obj.minRemoveToMakeValid_Method2("())()(((")
print("output", result)

# Method of solving

# Method 1: 
# Pretty straightforward, use a stack to keep track of opening parenthesis, then when an invalid one is found,
# append its index to a list. After iterating through the string, iterate in reverse through invalid index array,
# removing from the string each invalid index. Iterate in reverse to avoid messing up the indices which are invalid.
