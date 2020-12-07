'''
    https://www.acmicpc.net/problem/10026
    단순한 DFS문제 다만 적록색약에 따른 경우의 수만 체크
    
'''

import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(9999)


N = int(input())

data = []

for _ in range(N):

    data.append(list(input().strip()))

visited = {}
def dfs(i,j,Color):

    visited[(i,j)] = 1

    #자 이제 시작이야 피카츄 !

    #다음은 4방향 퍼트리기

    if i + 1 < N and not (i+1,j) in visited:
        if data[i+1][j] == Color:
            dfs(i+1,j,Color)

    if j + 1 < N and not (i,j+1) in visited:
        if data[i][j+1] == Color:
            dfs(i,j+1,Color)

    if i - 1 >= 0 and not (i-1,j) in visited:
        if data[i-1][j] == Color:
            dfs(i-1,j,Color)

    if j - 1 >= 0 and not (i,j-1) in visited:
        if data[i][j-1] == Color:
            dfs(i,j-1,Color)

commonCount = 0
for i in range(N):
    for j in range(N):

        if not (i,j) in visited:
            commonCount +=1
            dfs(i,j,data[i][j])

handicapCount = 0
visited = {} #초기화

for i in range(N):
    for j in range(N):
        if data[i][j] == 'G':
            data[i][j] = 'R'

for i in range(N):
    for j in range(N):

        if not (i,j) in visited:
            handicapCount +=1
            dfs(i,j,data[i][j])

print(commonCount,handicapCount)