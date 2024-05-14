# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pcount, ncount, zcount = 0, 0, 0
    for item in arr:
        if item > 0:
            pcount += 1
        elif item < 0:
            ncount += 1 
        else: 
            zcount += 1
    total_items = len(arr)

    zfraction = "{{:.{}f}}".format(6).format(zcount / total_items)
    pfraction = "{{:.{}f}}".format(6).format(pcount / total_items)
    nfraction = "{{:.{}f}}".format(6).format(ncount / total_items)
    print(pfraction)
    print(nfraction)
    print(zfraction)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
