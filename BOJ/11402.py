'''
    https://www.acmicpc.net/problem/11402

    루카스 정리를 이용하여 해결

'''

import math
import sys


sys.setrecursionlimit(9999)
input = sys.stdin.readline

'''
이항계수 3 은
페르마의 소정리
a^(p-1) === 1 mod p

(N!%p)( ((K!(N-K)!)^(P-2) )

이항계수 4는
루카스의 정리를 이용한다.

'''

dp = { (1,0) : 1, (1,1) : 1 }

def makeNbase(n,base):

    result = []
    while n > 0:
        result.append(n%base)
        n//=base
    return result

def bino(n,r,M):

    if r == 0 or n == r:
        dp[(n,r)] = 1
        return 1

    if (n,r) in dp:
        return dp[(n,r)]

    dp[(n,r)] = (bino(n-1,r,M) + bino(n-1,r-1,M) ) % M
    return dp[(n,r)]

N, K, M = [int(x) for x in input().strip().split()]



NM = makeNbase(N,M)
KM = makeNbase(K,M)


ret = 1

for i in range( max(len(NM),len(KM))):

    if i < len(NM):
        n = int(NM[i])
    else:
        n = 0

    if i < len(KM):
        k = int(KM[i])
    else:
        k = 0


    if n < k :
        ret = 0
        break

    ret *= bino(n,k,M) % M

print(ret % M)



