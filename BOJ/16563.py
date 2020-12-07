'''
    https://www.acmicpc.net/problem/16563

    단순구현으로 해결했지만...
    python3로는 통과하지 못 했음.

'''

import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())

#a~b 포함 사이 소수
def getPrimeNumberList(a,b):

    data = [True] * (b + 1)
    data[2] = True

    for i in range(2,b+1):

        if data[i] == True:

            for j in range(i+i,b+1,i):
                
                data[j] = False

    primes = [x for x in range(len(data)) if data[x] and x >= a ]
    return primes

primes = getPrimeNumberList(2,int(math.sqrt(5000000)+1))

def print_factor(n):

    idx = 0

    ans = []

    while n > 1 and idx < len(primes):

        if n % primes[idx] == 0:
            ans.append(primes[idx])
            n //= primes[idx]

        else:
            idx+=1

    if idx == len(primes):
        ans.append(n)
    print(' '.join(map(str,ans)))

    

for i in input().strip().split():

    print_factor(int(i))