# 9372 - 상근이의 여행 // 신장트리
import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

t = int(input())

while t:
    n,m = map(int,input().split())
    parent = [i for i in range(n+1)]
    count = 0

    for _ in range(m):
        a,b = map(int,input().split())

        if find_parent(a)!=find_parent(b):
            union_parent(a,b)
            count+=1
    print(count)
    t-=1