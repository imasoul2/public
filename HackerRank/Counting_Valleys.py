#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    num_valley = 0 # init variables
    level = 0 # init sea level

    for i in range(0,steps):
        if path[i] == 'U':
            level += 1
            if level == 0: # since we know that we climbed up a "valley" when we return to sea level from climbing,
                num_valley +=1 # add the number of valleys by 1.

        elif path[i] == 'D':
            level -= 1
        
    return num_valley
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
