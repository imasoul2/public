#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    length_arr = len(c)
    index = 0
    jumps = 0

    while index != length_arr-1 :
        if index + 2 < length_arr:
            if c[index+2] != 1:
                index = index + 2
                jumps += 1
            else:
                index = index + 1
                jumps += 1
        elif index + 1 < length_arr:
            index = index + 1
            jumps += 1

    return jumps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
