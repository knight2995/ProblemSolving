'''

    https://www.acmicpc.net/problem/1963
    단순한 BFS
    

'''

import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(99999)

def getPrimeNumberList(a,b):

    data = [True] * (b + 1)
    data[2] = True

    for i in range(2,b+1):

        if data[i] == True:

            for j in range(i+i,b+1,i):
                
                data[j] = False
    
    primes = [x for x in range(len(data)) if data[x] and x >= a ]
    return primes

primes = getPrimeNumberList(1000,9999)

T = int(input())

def bfs(start,end):

    #None 문자열이 나을까 숫자로 하는게 나을까 ?
    visited = {}

    queue = deque()
    count = 0
    queue.append([start,count])
    visited[start] = 1


    while len(queue) != 0:
        
        v, count = queue.popleft()

        if v == end:
            return count

        #첫번째 자리 바꾸기
        c = v % 1000   #첫번재 자리만 날리기
        for i in range(1,10):
            temp = c + i * 1000
            if not temp in visited and temp in primes:
                queue.append([temp,count+1])
                visited[temp] = 1
        #두번째 자리 바꾸기
        c = v - 100 * ((v % 1000) // 100)
        for i in range(0,10):
            temp = c + i * 100
            if not temp in visited and temp in primes:
                queue.append([temp,count+1])
                visited[temp] = 1

        #세번째 자리 바꾸기
        c = v - 10 * ((v % 100) // 10)
        for i in range(0,10):
            temp = c + i * 10
            if not temp in visited and temp in primes:
                queue.append([temp,count+1])
                visited[temp] = 1

        #네번째 자리 바꾸기
        c = v - (v % 10)
        for i in range(0,10):
            temp = c + i
            if not temp in visited and temp in primes:
                queue.append([temp,count+1])
                visited[temp] = 1

    return "Impossible"



for _ in range(T):

    start, end = map(int,input().split())

    print(bfs(start,end))