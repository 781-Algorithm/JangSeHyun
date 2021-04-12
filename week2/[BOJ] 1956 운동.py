# 1956 - 운동
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline


def dijkstra(start):
    
    distance = [INF] * (v + 1)
    q = []

    for next,value in graph[start].items():
        distance[next] = value
        heappush(q,[distance[next],next])

    while q:
        dist, now = heappop(q)

        if now == start:
            return dist

        if distance[now] < dist:
            continue

        for next,value in graph[now].items():
            cost = value + dist
            if distance[next] > cost:
                distance[next] = cost
                heappush(q, [cost, next])

    return INF

v,e = map(int,input().split())
INF = 1e9
graph = [{} for _ in range(v+1)]
cycle_cost = INF

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(v+1):
    cycle_cost = min(cycle_cost,dijkstra(i))

print(cycle_cost if cycle_cost!=INF else -1)