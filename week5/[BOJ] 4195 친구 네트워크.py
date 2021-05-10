# 4195 - 친구 네트워크 // 좀 빡셈. 어떻게 카운트를 할 것인가에 대해
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x]) # 경로 압축.
    return parent[x]

def union_parent(parent,x,y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)

    if x != y:
        parent[y] = x
        count[x] += count[y] # 달라지는 부분
    print(count[x])
    return

t = int(input())

while t:
    f = int(input())
    parent = {}
    count = {}
    for i in range(f):
        a, b = input().rstrip().split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        union_parent(parent,a,b)

    t-=1