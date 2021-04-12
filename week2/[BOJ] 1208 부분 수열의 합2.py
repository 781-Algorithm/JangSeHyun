# 1208 - 부분수열의 합 2 // 이분 탐색보다는 차라리 딕셔너리 쓰는게 어때..?
from bisect import bisect_right, bisect_left
n,s = map(int,input().split())
lst = list(map(int,input().split()))
arr1, arr2 = lst[:n//2], lst[n//2:]
temp1,temp2 = [0],[0]

for i in range(n//2):
    temp = []
    for j in temp1:
        temp.append(j+lst[i])
    temp1+=temp

for i in range(n//2,n):
    temp= []
    for j in temp2:
        temp.append(j+lst[i])
    temp2+=temp

temp2.sort()
result = 0

for i in temp1:
    result += (bisect_right(temp2,s-i)-bisect_left(temp2,s-i))

if s == 0:
    print(result-1)
else:
    print(result)