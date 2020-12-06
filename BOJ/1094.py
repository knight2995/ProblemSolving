'''
    https://www.acmicpc.net/problem/1094

    문제는 복잡하지만 결국은 2로 나눴을 때 나눠지지 않는 숫자와 같다.
    = 이진수로 변환하고 1의 갯수와 동일하다

'''

print(bin(int(input())).count('1'))