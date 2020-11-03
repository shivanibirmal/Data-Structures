
def convert_min_to_hrs(mins):
    if mins < 60:
        print( str(mins) + " mins")
    else:
        hrs = mins // 60
        mins_left = mins % 60

        print (str(hrs) + " hrs " + str(mins_left) + " mins")

# convert_min_to_hrs(34)
# convert_min_to_hrs(75)
# convert_min_to_hrs(150)
# convert_min_to_hrs(200)
# convert_min_to_hrs(0)

def string_reverse(s):
    reversed_string2 = s[::-1]
    print("reversed string 1 is", reversed_string2)

    reversed_string = ""
    for char in range(len(s)-1, -1, -1):
        reversed_string = reversed_string + s[char]

    print("reversed string 2 is", reversed_string)

    reversed_string3 = "".join(reversed(s))
    print("reversed string 3 is", reversed_string3)

# string_reverse("")

def remove_duplicates(arr):
    my_set = set(arr)
    print("initial list:", arr)
    print("Unique elements list:" ,list(my_set))

    arr = sorted(arr)
    i = 0
    j = 1
    result = []
    while( j < len(arr)):
        if arr[i] == arr[j]:
            result.append(arr[i])
        i += 1
        j += 1
    print("repeated elements are: ", result)

    my_dictionary = {}
    for element in range(0, len(arr)):
        if arr[element] in my_dictionary:
            my_dictionary[arr[element]] += 1
        else:
            my_dictionary[arr[element]] = 1
    print("my_dictionary:", my_dictionary)

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Input: s = "()[]{}"
# Output: true
def parenthesis(s):
    open_brackets = ["(", "[" ]
    closed_brackets = [")", "]"]

    if s == "":
        return True
    if len(s) % 2 != 0:
        return False
    st = []
    for char in s:
        if s in open_brackets:
            st.append(s)
        elif st and open_brackets.index(st[-1]) == closed_brackets.index(char):
            st.pop()
        else:
            return False
    return st == []






l = [1,2,3,22,3,55,66,1]
remove_duplicates(l)

