'''
    https://www.acmicpc.net/problem/15686
    치킨 거리를 구하고 DPS로 완전탐색을 하면 된다.

'''


import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline



N, M = map(int,input().split())

data = []

for _ in range(N):
    data.append([int(x) for x in input().split()])

houses = []
chickens = []

def getChickenDistance(houses, chickens, indexList):

    selectedChickens = [chickens[x] for x in indexList ]

    ret = 0
    for house in houses:
        temp = []
        for chicken in selectedChickens:
            temp.append( abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]) )
        
        ret += min(temp)

    return ret



for row in range(N):
    for col in range(N):
        if data[row][col] == 1:
            houses.append((row,col))
        elif data[row][col] == 2:
            chickens.append((row,col))

Index = [x for x in range(len(chickens))]
selectedIndex = []

ans = N ** 3
def dfs(idx,houses,chickens):
    global ans
    global selectedIndex

    if len(selectedIndex) == M:
        temp = getChickenDistance(houses,chickens,selectedIndex)
        ans = min(temp,ans)
        #
    else:

        for i in range(idx,len(Index)):

            selectedIndex.append(i)
            dfs(i+1,houses,chickens)
            selectedIndex.pop()

dfs(0,houses,chickens)
print(ans)