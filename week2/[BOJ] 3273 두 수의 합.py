# 3273 - 두 수의 합 ( 투 포인터 이지만, 양쪽 끝에서 오는 방법이 있음)
from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
arr.sort()

temp_sum = 0
start, end, result = 0, n-1, 0

while start<end:

    temp_sum = arr[start]+arr[end]

    if temp_sum > x:
        end-=1

    elif temp_sum < x:
        start+=1

    else:
        result+=1
        start+=1

print(result)