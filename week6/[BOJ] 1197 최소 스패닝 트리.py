# 1197 - 최소 스패닝 트리
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

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
graph, total = [], 0
for _ in range(e):
    graph.append(tuple(map(int, input().split())))

graph.sort(key=lambda x: x[-1])

for road in graph:
    a,b,cost = road
    if find_parent(a)!=find_parent(b):
        union_parent(a,b)
        total+=cost

print(total)
