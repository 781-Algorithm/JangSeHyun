# 1644 - 소수의 연속합 ( 소수판별 알고리즘이 더해짐 )
from sys import stdin
from math import sqrt

input = stdin.readline
n = int(input())
prime_num = [True]*(n+1)

if n == 1:
    print(0)
else:
    for i in range(2,int(sqrt(n))+1):
        if prime_num[i]==True:
            j = 2
            while i*j <= n:
                prime_num[i*j] = False
                j+=1
                # 얘를 for문으로 하고, range 3번째 파라미터를 i로 주면 더 빠르게 간다.
                # 그리고 *2부터 볼 필요가 없는게, i*i부터 가도 맞음. 이유는?

    arr = [] 
    length = 0
    for i in range(2,n+1):
        if prime_num[i]:
            arr.append(i)
            length+=1

    end, temp, result = 0, 0, 0

    for start in range(length):
        while temp < n and end < length:
            temp += arr[end]
            end+=1
        if temp == n:
            result+=1
        temp-=arr[start]

    print(result)