# 2470 - 두 용액
from sys import stdin
input = stdin.readline

n = int(input())
solution = list(map(int,input().split()))
solution.sort()

temp, start, end, value = 0, 0, n-1, 1e10
s_index,e_index = 0, 0

while start < end:

    temp = solution[start] + solution[end]
    if abs(temp) < value:
        s_index = start
        e_index = end
    value = min(value, abs(temp))

    if temp < 0:
        start+=1

    else:
        end -= 1

print(solution[s_index],solution[e_index])