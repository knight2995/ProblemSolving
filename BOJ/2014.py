'''
    https://www.acmicpc.net/problem/2014
    단순 구현..
    
'''

import math
import sys
import copy

input = sys.stdin.readline

K,N = list(map(int,input().strip().split()))

Primes = [int(x) for x in input().strip().split()]

import heapq

heap = copy.deepcopy(Primes)

while True:

    ret = heapq.heappop(heap)
    for p in Primes:
        heapq.heappush(heap,p*ret)
        if ret % p == 0:
            break
        

    N-=1
    if N == 0:
        break

print(ret)