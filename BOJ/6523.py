'''
    https://www.acmicpc.net/problem/6523

    단순 구현

'''

import sys


def find(N,a,b):


    data = {}

    c = 0

    drink = 0
    while True:

        if c in data:
            data[c] += 1
        else:
            data[c] = 1

        if data[c] == 3:
            break
        elif data[c] == 2:
            drink +=1
        
        c = (a * c ** 2 + b) % N

    return N - drink

while True:
    s = sys.stdin.readline().split()
    if s[0] == '0':
        break
    N, a, b = list(map(int,s))

    print(find(N,a,b))

    

