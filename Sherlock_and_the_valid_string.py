#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
# def isValid(s):
#     # My 15/20 correct code:
#     occurence_list=sorted(Counter(s).values())
#     if len(occurence_list)==0 or (occurence_list[-1] - occurence_list[0]==1)  or (occurence_list[-1]==occurence_list[0]): return 'YES'
#     # elif occurence_list[0]==1 and occurence_list[1:]!=1: return 'YES'
#     else:return 'NO'
#     # return str(occurence_list)

# Code without using collections.Counter:
def isValid(s):
    #Create a list containing just counts of each distinct element
    freq = [s.count(letter) for letter in set(s) ]
    #If all values the same, then return 'YES'
    if max(freq)-min(freq) == 0:
        return 'YES'
    #If difference between highest count and lowest count is 1
    #and there is only one letter with highest count, 
    #then return 'YES' (because we can subtract one of these 
    #letters and max=min , i.e. all counts are the same)
    elif freq.count(max(freq)) == 1 and max(freq) - min(freq) == 1:
        return 'YES'
    #If the minimum count is 1
    #then remove this letter, and check whether all the other
    #counts are the same
    elif freq.count(min(freq)) == 1:
        freq.remove(min(freq))
        if max(freq)-min(freq) == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
