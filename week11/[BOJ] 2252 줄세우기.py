# 2252 줄세우기
from sys import stdin
from collections import deque
input = stdin.readline

def topology_sort():

    q = deque()
    for i in range(1,n+1):
        if not in_degree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            in_degree[i] -= 1
            if not in_degree[i]:
                q.append(i)

n, m = map(int,input().split())
in_degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    in_degree[b] += 1
topology_sort()