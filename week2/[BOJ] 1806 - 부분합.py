# 1806 - 부분합 ( 양끝에서 움직이는게 아니라, 한쪽에서 같이 움직일 때)
from sys import stdin
input = stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

end, temp, length = 1, arr[0], 1e9

for start in range(n):

    while temp < s and end < n:
        temp += arr[end]
        end+=1

    if temp >=s:
        length = min(length, end-start)

    temp -= arr[start]

print(0 if length == 1e9 else length)