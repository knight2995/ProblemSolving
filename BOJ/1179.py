'''
    https://www.acmicpc.net/problem/1179
    dp를 이용한 요세푸스 문제 해결

'''

import sys,math
input = sys.stdin.readline

sys.setrecursionlimit(9999)

N, K = list(map(int,sys.stdin.readline().split()))

dp = {}
def josephus(n):
    
    global K

    if n == 1:
        return 0

    if K == 1:
        return n-1

    if n in dp:
        return dp[n]

    if K <= n:
        n2 = n - n // K
        dp[n] = K * (( ( josephus(n2) - n % K) ) % n2) // (K -1)
        return dp[n]
    else:
        dp[n] = (josephus(n-1) + K) % n
        return dp[n]

print(josephus(N) + 1)

