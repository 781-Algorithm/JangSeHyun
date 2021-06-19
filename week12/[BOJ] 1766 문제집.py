# 1766 문제집
from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

def topology_sort():
    
    q = []
    result = []
    for i in range(1, n + 1):
        if not in_degree[i]:
            heappush(q, i)

    while q:
        cur = heappop(q)
        result.append(cur)
        for next in graph[cur]:
            in_degree[next] -= 1
            if not in_degree[next]:
                heappush(q, next)

    print(*result)
    return

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

topology_sort()