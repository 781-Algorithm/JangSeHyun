# 17298 - 오큰수
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
result = [-1]*n
stack = []

for idx, value in enumerate(arr):

    if not stack or value<arr[stack[-1]]:
        stack.append(idx)
        continue

    while stack and value>arr[stack[-1]]:
        result[stack.pop()] = value
    stack.append(idx)

print(*result)