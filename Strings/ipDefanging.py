import sys

def ipDefang(s):
    res = ""
    for ch in s:
        if ch == '.':
            res = res + '[' + ch + "]"
        else:
            res += ch
    return res

str = input("Enter the ip address: ")
defangedIp = ipDefang(str)
print ("Defanged ip: ", defangedIp)
