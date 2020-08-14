# For some info: https://www.hackerrank.com/challenges/two-strings/topics/string-basics
def twoStrings(s1, s2):
# My Solution; I can't believe I did this in the first attempt!
    substring=[]
    for i in s1:
        if i in s2: substring.append(i)
    if substring!=[]: return 'YES'
    else: return 'NO'

# Faster solution using sets. Sets use hash tables as underlying data structure
    # s1 = set(s1)
    # s2 = set(s2)
    # result = s1.intersection(s2)
    # if not result: return 'NO'
    # else: return 'YES'

# Single Line Solution:
    # return 'YES' if set(s1) & set(s2) else 'NO