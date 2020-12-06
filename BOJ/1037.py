'''

    https://www.acmicpc.net/problem/1037
    
    답 = gcd * lcm


'''


import math, sys
input = sys.stdin.readline

def gcd(l):
    ret = l[0]
    for i in l[1:]:
        ret = math.gcd(ret,i)

    return ret

def lcm(l):
    ret = l[0]
    for i in l[1:]:
        ret = (ret * i) // math.gcd(ret,i)
    return ret

t = int(input())

l = list(map(int,input().split()))

print(gcd(l) * lcm(l))