'''
    https://www.acmicpc.net/problem/2436

'''


import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

#9 , 90 이라고 하면
#C = 10
#c = 3
# 1 , 10
# 2, 5      18 45
# 3, 

A,B = map(int,input().split())

#둘다 A의 배수
#A*a , A*b
#A * A * a * b // A = B
#A * a * b = B
#a * b = 30의 배수
#a = 5, b = 6


C = B // A
c = int(math.sqrt(C))

ret = []

for i in range(1, c+1):
    if C % i == 0:
        if math.gcd(i,C // i) == 1:
            ret = [i, C // i]


print(ret[0] * A , ret[1] * A)


