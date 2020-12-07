'''
    https://www.acmicpc.net/problem/16563
    단순 구현

'''


import sys,math
import re
import copy



N,L = [int(x) for x in input().strip().split()]

data = []

for i in range(N):
    inp = int(input())
    data.append(inp)

left_distance = 0
left_idx = 0

right_distance = 0
right_idx = 0

SSS = []

for i in range(len(data)):

    #오른쪽으로 가는 친구
    if data[i] >= 0:
        if L - data[i] > right_distance:
            right_idx = i
            right_distance = L - data[i]
    else:
        
        if abs(data[i]) > left_distance:
            left_idx = i
            left_distance = abs(data[i])

    SSS.append( [i,abs(data[i])])
 
SSS.sort(key=lambda x : x[1])

left = len([x for x in data if x < 0])

if left_distance < right_distance:
    print(SSS[left][0] +1,right_distance)
else:
    print(SSS[left-1][0]+1,left_distance)


