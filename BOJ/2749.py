'''
    https://www.acmicpc.net/problem/2749

    특정수의 모듈러 연산을 수행한 피보나치는 일정한 주기를 가진다.

'''

import math
import sys
from collections import deque

input = sys.stdin.readline



n = int(input())

period = 15 * 10**5

dp = {0:0,1:1,2:1}

for i in range(3,period+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10**6

print(dp[n%period])
