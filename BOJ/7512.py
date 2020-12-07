'''
    https://www.acmicpc.net/problem/7512
    슬라이딩 윈도우 기법으로 풀었다.


'''

import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

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

primes = getPrimeNumberList(2,10**7+1)


t = int(input())


def foo(n):

    #윈도우 포인터로 간다 !

    ret = []

    left = 0
    right = n

    s = sum(primes[:n])
    for _ in range(left, len(primes)-n):
        s = s + primes[right] - primes[left]
        left +=1
        right+=1
        ret.append(s)

    return ret

for testcase in range(t):

    m = int(input())

    data = [int(x) for x in input().split()]

    retList = []

    for d in data:
        retList.append(foo(d))

    #중복되는 값을 찾으면 된다
    notD = set(primes)
    for ret in retList:
        notD = notD & set(ret)

    print("Scenario %d:" % (testcase+1))
    print(min(notD))
    print()
    



