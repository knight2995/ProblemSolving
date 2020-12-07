'''
    https://www.acmicpc.net/problem/1215
    말은 요세푸스 문제지만 실상은...
    이분탐색을 통해 구현함. 자세한 건 나중에 정리.
'''

import sys,math
input = sys.stdin.readline

def sss(left,right,inc,k):

    sum = 0
    
    start = k % right

    sum += start * (right-left)

    sum += inc * (right-left) * (right-left-1)//2  


    return sum

def my(n,k):


    ret = 0
    
    #n이 k보다 큰 경우에는 k * 갯수 만큼 합이 나오게 된다
    if n > k :
        ret += (n-k) * k
    
    '''
    if n < k:
        ret += k % n
    '''
    left = 1
    right = k

    pos = 1

    while True:

        left = k // (pos +1)
        right = k  // pos

        right = min(right,n)
        #print('v = ',left,right,pos, sss(left,right,pos,k))

        if left <= n:
            ss = sss(left,min(right,n),pos,k)
            ret+= ss
        pos += 1

        if pos >= math.sqrt(k):
            ret += find(min(n,left),k)
            return ret
    

    return ret


def find(n,k):

    r = 0
    for i in range(1,n+1):
        #print(k,'%',i,'=',k%i)
        r = r + (k % i)
        

    return r

n, k = list(map(int,input().split()))

#ret = find(n,k)
m = my(n,k)


#print(ret,m)
print(m)

'''
N = 100 (나누는 수 mod m)
K = 100 (나눠지는 수)

소수 2,3,5,7,11 을 기준으로 할 때

소수 2 기준
100 - (51-100) = 1 * 값 % N
50 - (34-50) = 2 * 값 % N

1씩 증가하는 값들의 범위 + 2씩 증가하는 값들의 범위 + 3씩 증가하는 값들의 범위




'''


'''
F(N) = 1...N MOD i

'''

'''
K = 고정이라 하면
K = 적당한 후 15라 하자

F(1) = 15 % 1 = 0
F(2) = 15 % 1 + 15 % 2 = 0 + 1 = 0


'''