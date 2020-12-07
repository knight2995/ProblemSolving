'''
    https://www.acmicpc.net/problem/2553
    단순하게 푸니 통과...

'''


import sys,math
input = sys.stdin.readline


N = int(input())

ret = 1
for i in range(1,N+1):
    ret *= i
    ret %= 10000000
    while ret%10==0:
        ret//=10

print(str(ret)[-1])