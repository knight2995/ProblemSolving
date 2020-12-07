'''
    https://www.acmicpc.net/problem/2042
    세그먼트트리를 이용한 구간합
'''

import sys,math
input = sys.stdin.readline

def init(index,start,end):


    if start == end:
        sTree[index] = data[start]
    else:
        mid = (start+end) // 2
        sTree[index] = init(index*2, start, mid) + init(index*2+1,mid+1,end)

    return sTree[index]

def update(index,start,end,targetIndex,diff):

    if targetIndex < start or targetIndex > end:
        return

    sTree[index] += diff

    if start != end:
        mid = (start+end) // 2
        update(index*2,start, mid,targetIndex, diff)
        update(index*2+1,mid+1,end,targetIndex, diff)

#start, end = 1과 N
def sumTree(index,start,end,left,right):

    if start > right or end < left:
        return 0
    elif start >= left and right >= end:
        return sTree[index]
    else:
        mid = (start+end) // 2
        return sumTree(index*2,start,mid,left,right) + sumTree(index*2+1,mid+1,end,left,right) 

'''
init(1,0,N-1)

print(sTree)
#Left 미포함
update(1,0,N-1,1,2)
print(sTree)
#print(sumTree(1,0,N-1,3,5))
'''


N,M,K = list(map(int,input().strip().split()))

data = []

sTree = [0] * (2**(int(math.ceil(math.log(N,2))) + 1))

for i in range(N):
    data.append(int(input()))

init(1,0,N-1)


for i in range(M+K):
    a, b, c = list(map(int,input().strip().split()))

    if a == 1:
        #변경
        diff = c - data[b-1]
        data[b-1] = c
        update(1,0,N-1,b-1,diff)

    else:
        print(sumTree(1,0,N-1,b-1,c-1))



