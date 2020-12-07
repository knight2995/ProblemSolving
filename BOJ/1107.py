'''
https://www.acmicpc.net/problem/1107

'''

import sys
import math
import copy
from collections import deque
input = sys.stdin.readline


N = int(input())
M = int(input())

errorBtn = set()
if M != 0:

    errorBtn = set([int(x) for x in input().split()])

btn = list(set([int(x) for x in range(10)]) - errorBtn)

def isValid(n,btn):

    #btn 조합으로 만들 수 있는가
    if n == 0:
        if 0 in btn:
            return 1
        else:
            return -1

    s = list(str(n))

    ret = 0
    for num in s:

        if int(num) in btn:
            ret+=1
        else:
            return -1

    return ret




ans = abs(N-100)



for i in range(0,1999999):

    count = isValid(i,btn)
    #print(i,count)
    if count != -1:
        ans = min(ans,count + abs(N-i))


print(ans)
