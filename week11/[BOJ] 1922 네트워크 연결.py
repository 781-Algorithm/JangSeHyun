# 1922 네트워크 연결
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal():
    total = 0
    graph.sort(key=lambda x: x[0])
    for cost, start, to in graph:
        if find_parent(start) != find_parent(to):
            union_parent(start,to)
            total += cost

    return total

n,m = int(input()), int(input())
parent = [i for i in range(n+1)]
graph = []
for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])

print(kruskal())