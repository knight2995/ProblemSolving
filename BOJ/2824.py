'''
    https://www.acmicpc.net/problem/2824

'''

import sys,math
import re

input = sys.stdin.readline


def getPrimeList(num):
    primes = []
    if num < 2:
        return primes
    for i in range(2, num+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
    return primes

primeList = getPrimeList(int(math.sqrt(10**10)))

def factor(n):

    global primeList
    result= {} 
    for i in primeList:
        if n < 2:
            break
        
        count=0
        while n%i==0:
            count+=1
            n= n//i
            if count!=0: 
                result[i] = count
    if n > 1:
        if n in result:
            result[n]+=1
        else:
            result[n]=1
    return result

N = int(input())

N_Data = [int(x) for x in input().strip().split()]

M = int(input())

M_Data = [int(x) for x in input().strip().split()]

N_factorize = {}
M_factorize = {}

for i in N_Data:

    fac = factor(i)
    for k in fac:
        if k in N_factorize:
            N_factorize[k] += fac[k]
        else:
            N_factorize[k] = fac[k]

for i in M_Data:

    fac = factor(i)
    for k in fac:
        if k in M_factorize:
            M_factorize[k] += fac[k]
        else:
            M_factorize[k] = fac[k]


ret = 1



keys = set(N_factorize.keys()) | set(M_factorize.keys())
for i in keys:

    A = 0
    if i in N_factorize:
        A = N_factorize[i]
    B = 0
    if i in M_factorize:
        B = M_factorize[i]

    
    ret *= (i ** min(A,B))


if len(str(ret)) > 9:
    li = list(str(ret))[-9:]
    print(''.join(li))

else:
    print(ret)
