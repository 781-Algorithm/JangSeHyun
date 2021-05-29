# 6198 옥상 정원 꾸미기
from sys import stdin
input = stdin.readline

n = int(input())
result, heights = [0 for _ in range(n)], []
for _ in range(n):
    heights.append(int(input()))

stack = []

for idx, value in enumerate(heights):

    while stack and value >= heights[stack[-1]]:
        elem_idx = stack.pop()
        result[elem_idx] = idx - elem_idx - 1

    stack.append(idx)
# 스택에 남아있는 값들에 대한 처리. (오름차순일 수밖에 없다.)
while stack:
    elem_idx = stack.pop()
    result[elem_idx] = n - elem_idx - 1

print(sum(result))
