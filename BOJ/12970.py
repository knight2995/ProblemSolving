'''
    https://www.acmicpc.net/problem/12970

'''

import sys,math
import re
import copy

N, K = [int(x) for x in input().split()]

def g(S):

    s = S
    if type(S) != list:
        s = list(S)

    length = len(s)

    ret = 0
    for i in range(length):
        if s[i] == 'A':

            for j in range(i+1,length):
                if s[j] == 'B':
                    ret+=1
            

    return ret


S = ['B'] * N

def dprint(S):
    if type(S) != list:
        print(S)

    else:
        print(''.join(S))


maxA = N // 2
maxB = N - maxA
maxAB = maxA * maxB


if K > maxAB:
    dprint(-1)

elif K == 0:
    S[-1] = 'A'
    dprint(S)

else:

    k = 0
    for i in range(N):

        if i * (N-i) >= K:
            
            break

        k+=1

    a_count = k-1
    for i in range(a_count):
        S[i] = 'A'

    b_count = N - a_count
    for i in range(b_count+1):
        tempS = copy.deepcopy(S)
        tempS[-i] = 'A'

        if g(tempS) == K:
            dprint(tempS)
            break

#print(S)