# 1005 ACM craft
from sys import stdin
from collections import deque
input = stdin.readline

def topology_sort():
    q = deque()
    w = int(input())
    times = [0 for _ in range(n+1)]

    for i in range(1,n+1):
        if not in_degree[i]:
            q.append((i, delay[i]))
            times[i] = delay[i]

    while q:
        cur, cost = q.popleft()
        for next in graph[cur]:
            in_degree[next] -= 1
            times[next] = max(times[next], cost+delay[next])
            if not in_degree[next]:
                q.append((next, times[next]))

    return times[w]

t = int(input())
while t:
    n, k = map(int,input().split())
    delay = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    in_degree = [0 for i in range(n+1)]
    for _ in range(k):
        a, b = map(int,input().split())
        graph[a].append(b)
        in_degree[b] += 1

    print(topology_sort())

    t -= 1