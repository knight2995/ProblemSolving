'''

    https://www.acmicpc.net/problem/1158

    요세푸스는 굉장히 유명한 문제이다.

    https://ko.wikipedia.org/wiki/%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4_%EB%AC%B8%EC%A0%9C

    일반해까지 존재하긴 하며, 이 문제는 전부 출력해야 하므로, 단순 구현으로 구현함.

'''


import sys


N, K = list(map(int,sys.stdin.readline().split()))


data = [i for i in range(1,N+1)]

point = -1

v = []
for i in range(N):

    point = (point + K ) % (N - i)
    v.append(data[point])
    del data[point]
    point -=1

print('<', end = '')
for i in range(len(v)-1):
    print(v[i], end=', ')
print(v[N-1], end=">")
