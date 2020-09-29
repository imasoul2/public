#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    answer = 0
    check_list = [0]*100 # create empty list to store the number of socks in 100 diff colours.
    counter = 0

    for i in range(1,101):
        for j in ar:
            if i == j: # if the colour matches the sock
                check_list[i-1] += 1 # increase the number of that colour list by 1
            if check_list[i-1] == 2: # if the num of socks is 2
                check_list[i-1] -= 2
                answer += 1 # delete the pair and increase the number of pairs by 1               
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
