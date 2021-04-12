# 11779 - 최소비용 구하기 2
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

def dijkstra(start):

    distance = [1e9]*1001
    distance[start] = 0
    q = []
    heappush(q,[0,start])

    while q:
        dist, now = heappop(q)
        if now == end:
            return dist

        for next, cost in graph[now].items():

            if distance[next] < cost:
                continue
            new_cost = cost + dist

            if new_cost < distance[next]:
                distance[next] = new_cost
                route_[next] = now
                heappush(q,[distance[next],next])

n = int(input())
m = int(input())
graph=[{} for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())

    if b in graph[a]:
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b]=c

start, end = map(int,input().split())
route_, result = [-1]*1001, []
print(dijkstra(start))
while True:
    result.append(end)
    if end == start:
        break
    end = route_[end]
print(len(result))
print(*result[::-1])