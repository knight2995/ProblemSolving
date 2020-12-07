'''
    https://www.acmicpc.net/problem/10422
    DP로 풀수도 있고
    아래 풀이 바법이 기억이 안난다.....
    나중에 작성할 것.
'''

import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(99999)

T = int(input())


def factorial(N):
    ret= 1
    for i in range(N):
        ret = ret * (i+1)
    return ret

def foo(L):

    if L % 2 == 1:
        return 0

    return (factorial(L) // (factorial(L//2) * ( (factorial((L//2)+1))))) % (10**9 +7 )

for _ in range(T):

    print(foo(int(input())))