import sys

def removeVowels(s):
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    res = ""
    for ch in s:
        if ch not in vowel_set:
            res += ch
            #print (ch, "present in the string, hence eliminating it.")
        # else:
        #     res += ch
    return res

str = input("Enter the string: ")
vowels_excluded_str = removeVowels(str)
print ("String with vowels removed: ", vowels_excluded_str)
