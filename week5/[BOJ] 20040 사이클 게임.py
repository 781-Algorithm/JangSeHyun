# 20040 - 사이클 게임 // 유니온 파인드로 사이클 판별
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,x,y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

n,m = map(int,input().split())
flag = False
over = 0
parent = [i for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())

    if not flag:
        if find_parent(parent,a) == find_parent(parent,b):
            flag=True
            over = i+1
        else:
            union_parent(parent,a,b)

print(over)