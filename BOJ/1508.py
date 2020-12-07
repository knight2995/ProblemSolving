'''
    https://www.acmicpc.net/problem/1508

    유사한 문제 - https://www.acmicpc.net/problem/2110 를 참고
'''

import math
import sys
import heapq

input = sys.stdin.readline


N, M, K = [int(x) for x in input().strip().split()]

data = [int(x) for x in input().strip().split()]

#data와 distance가 주어지면
#최대 몇개를 담을 수 있는 지 가르쳐줌
def getPickCount(data,dis,C):

    #거리가 i 일 때 왼쪽부터 하나씩 체크해나가보자
    #첫번재 좌표를 선택하는 것은 무조건 이득
    pick = [0]

    for j in range(1,len(data)):

        if data[j] - data[pick[-1]] >= dis:
            pick.append(j)
        
        if len(pick) == C:
            break
    
    #print('dis = ',dis, ' = ',pick)
    return len(pick) , pick
        


def find(data,C):

    maxDis = max(data) - min(data)
    #이분탐색
    left = 0
    right = maxDis

    l = 0
    ret = None

    while left <= right:

        mid = (left+right) // 2

        lc , pick = getPickCount(data,mid,C)
        if lc >= C :
            #mid를 올리면 된다.
            ret = pick
            l = mid
            left = mid + 1
            
        else:
            right = mid - 1

    return l,ret



#심판이 최소 2명이 가능하다 왜냐 ? 거리 계산이 필요하니까
#최대 거리가 중요한게 아니라
#심판 선택 수가 중요한 문제 였던 것이와요 아닌가 ?
#사실상 M이 K 이상인 것은 별로 중요하지 않다
#만약 중복 된 다면 최대 거리를 0이라고 해야 할 것 같다.

#비둘기 집의 원리로 인해 무조건 111이 될 것이다
if M >= K:
    print(''.join(['1' for _ in range(K)]))

elif M == 1:
    print(''.join(['1'] + ['0' for _ in range(K-1)]))

elif max(data) == min(data):

    print( ''. join (   ['1' for _ in range(M)] + ['0' for _ in range(K-M)]             ))
else:

    answer = ['0'] * K
    for i in range(1, M+1):

        #최장거리 찾기

        #print(i,'명 =',find(data,i))

        ret = find(data,i)

        temp = ['0'] * K

        for i in ret[1]:
            temp[i] = '1'

        if int(''.join(temp)) > int(''.join(answer)):
            answer = temp

    print(''.join(answer))