'''
    https://www.acmicpc.net/problem/2226
    단순한 DP

'''


import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())

#1 - 1개 01
#2 - 1개 1001
#3 - 3개 01101001
#4 - 5개 
#5 - 11개
#6 - 21개
# 이전의 01 갯수에 따라 바뀌는거 같은데 ?
#F(n) = F(n) * 2 // 짝 홀에 따라

start = 1
for i in range(1,N-1):

    if i % 2 == 1:
        start = start * 2 - 1
    else:
        start = start * 2 + 1
if N == 1:
    start = 0
print(start)