# 11438 LCA2 - pypy3로 통과..
import sys
from math import log2
from collections import deque
input = sys.stdin.readline

def bfs(x):

    q = deque()
    q.append((x,0))
    visited[x] = True

    while q:
        cur, count = q.popleft()

        for next_ in graph[cur]:
            if visited[next_]:
                continue
            visited[next_] = True
            depth[next_] = count + 1
            parent[next_][0] = cur
            q.append((next_, count+1))

def lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x
    for i in range(size-1, -1, -1):
        if depth[y] - depth[x] >= (1 << i):
            y = parent[y][i]

    if x == y:
        return x

    for i in range(size-1,-1,-1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]

    return parent[x][0]


n = int(input())
size = int(log2(n)) + 1
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
parent = [[0 for _ in range(size)] for __ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

for i in range(1, size):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))