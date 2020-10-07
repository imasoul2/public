#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    quotients_ans = 0
    remainder_ans = 0
    str_len = len(s)
    quotients = n//str_len
    remainder = n%str_len

    for i in range(0,remainder):
        if s[i] == 'a':
            remainder_ans +=1

    for i in s:
        if i == 'a':
            quotients_ans += 1

    answer = quotients_ans*quotients + remainder_ans

    return answer

        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
