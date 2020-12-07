'''
    https://www.acmicpc.net/problem/11025
    요세푸스 문제의 일반해를 이용하여 해결.
    
'''

import sys


N, K = list(map(int,sys.stdin.readline().split()))


#f(n) = (( f(n-1) + k -1) % n ) + 1

def f(n,k):

    if n == 1:
        return 1

    return (f(n-1,K) + k  - 1 ) % n + 1

def find(n,k):

    c = 1

    for i in range(1,n+1):
        c = ((c + k - 1) % i) + 1
        
    return c


print(find(N,K))

