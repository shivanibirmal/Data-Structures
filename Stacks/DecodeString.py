# 394. Decode String
# Medium
#
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
#
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
#
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

class Solution:
    def decodeString(self, s: str) -> str:

        if len(s) == 0:
            return ""
        int_stack = []
        char_stack = []
        brackets = ['[',  ']']
        num = ""

        for i in s:
            # print("current i:", i)
            if i in brackets:
                if i == '[':
                    # print("Pushing", num,"to int stack")
                    int_stack.append(int(num))
                    num = ""
                    char_stack.append(i)
                    # print(i,"pushed to char")
                else:
                    k = 0
                    if(len(int_stack) != 0):
                        k = int_stack.pop()

                    char = ""
                    while(True):
                        top = char_stack.pop()
                        # print("top:", top)
                        if top != '[':
                            char = top + char
                        else:
                            break
                    # print("chars before repeating", k, "times:", char)
                    if k > 0:
                        var = ""
                        while k > 0:
                            var += str(char)
                            k -= 1
                        char_stack.append(var)

                    else:
                        char_stack.append(char[::-1])

                    # print("char_stack:",char_stack)

            elif i.isalpha():
                char_stack.append(i)
                # print(i,"pushed to char")
                # print("after pushing char:", char_stack)
            elif i.isnumeric():
                num += i
                # print("num:",num)

        # print("char stack after for:", char_stack)
        # print("int stack after for:", int_stack)

        return "".join(char_stack)

s = "3[a]2[bc]"
obj = Solution()
result = obj.decodeString(s)
print("Decoded string:", result)

s2 = "10[ab]"
result = obj.decodeString(s2)
print("Decoded string:", result)

# Method solving:

# Maintain 2 separate stacks, one for int, one for characters. Push to char stack when either an opening bracket
# is encountered or a character. CANNNOT Push directly to int stack when a number is encountered since the number be
# of more that 1 digit. Hence, maintain a var to keep on concatenating the numbers encountered till we get an opening bracket.
# Once an opening bracket is found, push the concatenated number to int stack and make the variable empty for next number.
# When a closing bracket is found, pop char stack till opening bracket. maintain the order of the chars popped.
# Pop from int stack for check the repetation count for popped chars. concatenate all the popped chars and push
# them to char stack repetation count times. After parsing the entire string, return all the characters from the char stack.
