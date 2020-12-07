'''
    https://www.acmicpc.net/problem/14500
    ㅗ 모양을 제외하고는 DP로 풀 수 있다.

'''

import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline


#dfs로 풀어도 될 것 같다. 일단 브루트포스

N, M = [int(x) for x in input().split()]

data = []
for _ in range(N):
    data.append([int(x) for x in input().split()])

#(row,col) 
blocks = [
    [(0,0),(1,0),(2,0),(3,0)],  #1-자 세로
    [(0,0),(0,1),(0,2),(0,3)],  #1-자 가로

    [(0,0),(0,1),(1,0),(1,1)],  #정사각형

    [(0,0),(1,0),(2,0),(2,1)],  #L자 기본
    [(0,0),(1,0),(2,0),(2,-1)], #L자 대칭
    [(0,0),(1,0),(0,1),(0,2)],  #r 형태
    [(0,0),(0,1),(0,2),(1,2)],  #ㄱ 형태
    [(0,0),(1,0),(1,1),(1,2)],  #ㄴ 형태
    [(0,0),(0,1),(0,2),(-1,2)], #ㄴ 대칭형태
    [(0,0),(0,1),(1,1),(2,1)],  #ㄱ 긴거 반대
    [(0,0),(1,0),(2,0),(0,1)],  #위에 거 대칭

    [(0,0),(0,1),(1,1),(0,2)],  #ㅜ 형태
    [(0,0),(0,1),(-1,1),(0,2)], #ㅗ 형태
    [(0,0),(1,0),(1,1),(2,0)],  #ㅏ 형태
    [(0,0),(1,0),(1,-1),(2,0)], #ㅓ 형태

    [(0,0),(1,0),(1,1),(2,1)],  #잘 모르겠음 
    [(0,0),(0,1),(-1,1),(-1,2)],    #으
    [(0,0),(1,0),(1,-1),(2,-1)],
    [(0,0),(0,1),(1,1),(1,2)]
]

ret = 0

def foo(row,col):

    ret = -1

    for block in blocks:
        s = 0

        for pos in block:
            if 0 <= row + pos[0] < N and 0 <= col + pos[1] < M:
                s += data[row+pos[0]][col+pos[1]]
            else:
                s -= 9999
        
        ret = max(s,ret)

    return ret




for i in range(N):
    for j in range(M):
        v = foo(i,j)
        ret = max(ret,v)

print(ret)