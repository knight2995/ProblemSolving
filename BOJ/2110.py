'''
    https://www.acmicpc.net/problem/2110
    참고 참고
'''

import math
import sys
import heapq

input = sys.stdin.readline


N, C = [int(x) for x in input().strip().split()]

data = []

for i in range(N):
    data.append(int(input()))


data.sort()


#data와 distance가 주어지면
#최대 몇개를 담을 수 있는 지 가르쳐줌
def getPickCount(data,dis):



    #거리가 i 일 때 왼쪽부터 하나씩 체크해나가보자
    #첫번재 좌표를 선택하는 것은 무조건 이득
    pick = [data[0]]

    for j in range(1,len(data)):

        if data[j] - pick[-1] >= dis:
            pick.append(data[j])
    
    #print('dis = ',dis, ' = ',pick)
    return len(pick)
        

def find(data,C):

    maxDis = max(data) - min(data)

    #이분탐색
    left = 1
    right = maxDis

    ret = 0

    while left <= right:

        mid = (left+right) // 2

        if getPickCount(data,mid) >= C:
            #mid를 올리면 된다.
            ret = mid
            left = mid + 1
            
        else:
            right = mid - 1

    return ret





print(find(data,C))