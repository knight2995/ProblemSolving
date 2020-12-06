'''
    https://www.acmicpc.net/problem/1059

    적절한 구간 LuckySet이 존재 할 때, 조건 3가지를 따져보면 된다. 그 외는 간단한 구현 문제.

    #0. N이 LuckySet에 포함 된 경우
    #1. N의 위치가 LuckySet 왼쪽에 존재하는 지
    #2. N의 위치가 사이에 있는 경우
    


'''


import math, sys
input = sys.stdin.readline

L = int(input())

LuckySet = list(map(int,input().split()))

N = int(input())

LuckySet.sort()

i = 0

def find(left, right,N):
    ret = 0
    for i in range(left, right+1):
        for j in range(i+ 1, right+1):
            if i <= N <= j:
                #print(i,j)
                ret+=1

    return ret

#구간 찾기
#0. N이 LuckySet에 포함 된 경우
#1. N의 위치가 LuckySet 왼쪽에 존재하는 지
#2. N의 위치가 사이에 있는 경우

if N in LuckySet:
    print(0)
elif N < LuckySet[0]:
    left = 1
    right = LuckySet[0]-1
    print(find(left,right,N))
else:
    left = -1
    right = -1
    for i in range(len(LuckySet)):
        if LuckySet[i] > N:
            left = LuckySet[i-1] + 1
            right = LuckySet[i] - 1
            break

    print(find(left,right,N))

