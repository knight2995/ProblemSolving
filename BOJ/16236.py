'''
    https://www.acmicpc.net/problem/16236

    BFS를 이용하여 구현

'''
import sys
import math
import heapq
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(99999)

N = int(input())


#아기 상어 뚜루뚜루루루
#BFS 말고 단순하게 구현해보고 싶다.
#통과가 되는지

data = []

for _ in range(N):
    data.append([int(x) for x in input().strip().split()])

def init(data,shark):

    for i in range(N):
        for j in range(N):
            if data[i][j] == 9:
                shark[0] = [i,j]
                return



def isEatingFish(data,sharks):

    for i in data:
        for j in i:
            if  0 <j < min(sharks[1],7):
                return True
    return False


def findDistance(data,shark,target):

    #shark에서 target 가는 최단 거리를 찾아봅시다
    dis = 0

    visited = {}
    queue = deque()

    queue.append((shark[0][0],shark[0][1], dis))
    visited[(shark[0][0],shark[0][1])] = 1

    while len(queue) != 0:


        row ,col , dis = queue.popleft()

        if (row,col) ==  target and 0 < data[row][col] < shark[1]:
            return dis

        #아래
        if row+ 1 < N and not (row + 1,col) in visited:
            if data[row+1][col] <= shark[1]:
                queue.append((row+1,col,dis+1))
                visited[(row+1,col)] = 1

        #위
        if row - 1 >= 0 and not (row - 1,col) in visited:
            if data[row-1][col] <= shark[1]:
                queue.append((row-1,col,dis+1))
                visited[(row-1,col)] = 1

        #오른쪽
        if col + 1 < N and not (row,col+1) in visited:
            if data[row][col+1] <= shark[1]:
                queue.append((row,col+1,dis+1))
                visited[(row,col+1)] = 1

        #왼쪽
        if col - 1 >= 0 and not (row,col-1) in visited:
            if data[row][col-1] <= shark[1]:
                queue.append((row,col-1,dis+1))
                visited[(row,col-1)] = 1

    return -1


def findAndEatingFish(data,shark):

    #여기서 데이터 수정이 이뤄진다.
    #1. 전체를 조회하면서
    #2. 가장 거리가 가까운 애들 추가
    #3. 와... 가는 길에 물고기 큰 애들 있으면 그 길로 못 간다...
    #4. 그러므로 저기서 저기까지 가는 최단 경로를 찾아야 한다...
    #5. 결국 bfs를 해야 하넹
    dp = {} # 거리
    for row in range(N):
        for col in range(N):
            if 0 < data[row][col] < min(shark[1],7):
                dis = findDistance(data,shark,(row,col))
                #가는 길이 없다면
                if dis == -1:
                    continue
                if dis in dp:
                    dp[dis] = dp[dis] + [[row,col]]
                else:
                    dp[dis] =[[row,col]]
    
    if len(dp) == 0:
        return None

    dp = list(sorted(dp.items()))

    li = dp[0][1]
    dis = dp[0][0]
    #누구를 잡아 먹을 것인가 ?
    #row가 작으면서 col또한 작은 애로
    li.sort()
    pos = li[0]

    #자 이제 상어가 잡아 먹고, 그 곳으로 이동할 것이다
    #상어의 기존 위치는 0으로
    data[shark[0][0]][shark[0][1]] = 0
    data[pos[0]][pos[1]] = 9

    shark[0] = pos
    shark[2] += 1

    if shark[1] == shark[2]:
        shark[1] += 1
        shark[2] = 0


    return dis
    
#상어 정보
shark = [[-1,-1],2,0] #좌표 row,col / 크기 / 먹은 생선 수

init(data,shark)

ret = 0

def pprint(data):
    print('-------start----')
    for i in data:
        print(i)
    print('-------end----')
while isEatingFish(data,shark):

    #pprint(data)
    #print('shark = ',shark)
    
    dis = findAndEatingFish(data,shark)

    if dis == None:
        break
    ret += dis


print(ret)
