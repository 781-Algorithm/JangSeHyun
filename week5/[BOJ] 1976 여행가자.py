# 1976 - 여행 가자
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,x,y):
    q = find_parent(parent, x)
    w = find_parent(parent, y)
    if q < w:
        parent[w] = q
    else:
        parent[q] = w

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j]:
            union_parent(parent,i+1,j+1)

routes = list(map(int, input().split()))
start = find_parent(parent,routes[0])

flag = True
for i in range(1,m):
    if find_parent(parent,routes[i])!=start:
        print("NO")
        flag = False
        break

if flag:
    print("YES")