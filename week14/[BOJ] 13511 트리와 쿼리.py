# 13511 트리와 쿼리 2
import sys, math
from collections import deque

input = sys.stdin.readline


def bfs(x):
    visited = [False for _ in range(n + 1)]
    visited[x] = True
    q = deque()
    q.append((x, 0, 0))

    while q:
        cur, count, cost = q.popleft()
        for node in graph[cur]:
            if visited[node]:
                continue
            visited[node] = True
            depth[node] = count + 1
            parent[node][0] = cur
            distance[node] = cost + graph[cur][node]
            q.append((node, count + 1, distance[node]))


def lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    for i in range(size - 1, -1, -1):
        if depth[y] - depth[x] >= (1 << i):
            y = parent[y][i]

    if x == y:
        return y

    for i in range(size - 1, -1, -1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]

    return parent[x][0]



n = int(input())
size = int(math.log2(n)) + 1
graph = [{} for _ in range(n + 1)]
depth = [0] * (n + 1)
parent = [[0]*size for _ in range(n+1)]
distance = [0] * (n+1)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

bfs(1)

for i in range(1,size):
    for j in range(1,n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

for _ in range(int(input())):
    query = list(map(int,input().split()))
    x, y = query[1], query[2]
    ans = lca(x, y)  # from x to y

    if query[0] == 1:
        print(distance[x] + distance[y] - 2*distance[ans])

    else:
        k = query[3]
        temp = depth[x] - depth[ans] + 1 # 시작점 ~ LCA까지 개수
        if temp == k:
            print(ans)
        elif temp > k:
            k -= 1
            for i in range(size-1,-1,-1):
                if k >= (1 << i):
                    x = parent[x][i]
                    k -= (1 << i)
            print(x)
        else:
            k -= temp  # 만큼 LCA에서 내려간 정점에 해당함.
            k = depth[y] - depth[ans] - k  # 올라가야할 개수 from y
            for i in range(size-1,-1,-1):
                if k >= (1 << i):
                    y = parent[y][i]
                    k -= (1 << i)
            print(y)