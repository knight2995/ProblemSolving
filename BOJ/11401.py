'''
    https://www.acmicpc.net/problem/11401

    페르마의 소정리를 이용한 문제 이후에 velog에 정리할 것

'''

import math
import sys

sys.setrecursionlimit(9999)

input = sys.stdin.readline

'''
페르마의 소정리
a^(p-1) === 1 mod p

(N!%p)( ((K!(N-K)!)^(P-2) )
'''


def power(A,B):

    ret = 1

    while B > 0:
        if B % 2 == 1:
            ret *= A
        A = ( A * A ) % (10**9 + 7)
        B//=2
    return ret % (10**9 + 7)

N, K = [int(x) for x in input().strip().split()]


ret = 1
fact = {0:1}
for i in range(N):
    fact[i+1] = (fact[i] * (i+1) ) % (10**9 + 7)


print( (fact[N] * power( fact[K] * fact[N-K] ,10**9+5 ) ) % (10**9+7))
