#
# Your previous Plain Text content is preserved below:
#
# ROT-13 ("rotate by 13 places") is a simple cipher that replaces a letter with the 13th letter after it in the alphabet (wrapping around if necessary). In this question, we will consider a generalization of ROT-13 algorithm. We will allow rotation of any non-zero distance.
#
# For example:
#     ROT-1('abc') == 'bcd'
#     ROT-3('hello') == 'khoor'
#     ROT-1('z') == 'a'
#
# Suppose you have a list of strings, e.g.,
#
#     ['anyscale', 'hello', 'abc', 'def', 'bcd', 'a', 'i']
#
# Write a program that returns the subset of words such that some rotated version of the word is also in the list. In this case, the program should return
#
#     ['abc', 'def', 'a', 'i', 'bcd']
#
# because ROT-3('abc') == 'def' and ROT-8('a') == 'i' (and similarly for 'def' and 'i').
def getMap(words):
    wordMap = {}
    for word in words:
        if wordMap.keys() is not []:
            if len(word) in wordMap.keys():
                wordMap[len(word)].append(word)
            else:
                wordMap[len(word)] = [word]
    return wordMap
def canRotate(wordList):
    # keyWord = wordList[0]
    ans=[]
    count = 0
    while count < len(wordList):
        keyWord = wordList[0]
        ans.append(keyWord)
        wordList.remove(keyWord)
        for i in range(1, 26):
            newWord = ""
            for letter in keyWord:
                newletter = chr(ord(letter) + i)
                newWord = newWord + newletter
            if newWord in wordList:
                ans.append(newWord)
                wordList.remove(newWord)
        count += 1
    return ans

def solution(words):
    wordMap = getMap(words)
    ans = []
    print(wordMap)
    for value in wordMap.values():
        if len(value) <= 1:
            continue
        res = canRotate(value)
        ans = ans + res
        #
        # if canRotate(value):
        #     ans = ans.append(value)
    return ans
print(solution(['anyscale', 'hello', 'abc', 'bcd', 'a', 'i', 'cab', 'dbc']))
