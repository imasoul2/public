#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numOfSwaps = 0
    tempArray = a
    temp = 0
    k = len(a) 
    loop_condition = 1

    while(loop_condition):
        loop_condition = 0
        for i in range(0,k-1):
            if tempArray[i] > tempArray[i+1]:
                temp = tempArray[i+1]
                tempArray[i+1] = tempArray[i]
                tempArray[i] = temp
                numOfSwaps += 1
                loop_condition = 1
        


    print("Array is sorted in {} swaps.".format(numOfSwaps))
    print("First Element: {}".format(tempArray[0]))
    print("Last Element: {}".format(tempArray[len(tempArray)-1]))
            


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
