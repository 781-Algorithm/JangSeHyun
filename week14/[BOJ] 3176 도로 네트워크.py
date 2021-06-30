# 3176 도로 네트워크 - pypy3로 통과
import sys, math
from collections import deque
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append([x, 0])
    visited[x] = True

    while q:
        cur, count = q.popleft()
        for nex, val in graph[cur].items():
            if visited[nex]:
                continue
            visited[nex] = True
            depth[nex] = count+1
            parent[nex][0][0] = cur
            parent[nex][0][1] = parent[nex][0][2] = val
            q.append([nex, count+1])

def lca(x,y):
    if depth[x] > depth[y]:
        x, y = y, x

    mini, maxi = math.inf, -1
    for i in range(size-1,-1,-1):
        if depth[y] - depth[x] >= (1 << i):
            mini = min(mini, parent[y][i][1])
            maxi = max(maxi, parent[y][i][2])
            y = parent[y][i][0]

    if x == y:
        return mini, maxi

    for i in range(size-1, -1, -1):
        if parent[x][i][0] != parent[y][i][0]:
            mini = min(mini, parent[x][i][1],parent[y][i][1])
            maxi = max(maxi, parent[x][i][2],parent[y][i][2])
            x = parent[x][i][0]
            y = parent[y][i][0]

    return min(mini, parent[x][i][1],parent[y][i][1]), max(maxi, parent[x][i][2], parent[y][i][2]),


n = int(input())
size = int(math.log2(n))+1
graph = [{} for _ in range(n+1)]
visited = [False]*(n+1)
depth = [0]*(n+1)
parent = [[[0,0,0] for __ in range(size)] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

bfs(a)

for i in range(1, size):
    for j in range(1, n+1):
        parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0]
        parent[j][i][1] = min(parent[j][i-1][1], parent[parent[j][i-1][0]][i-1][1])
        parent[j][i][2] = max(parent[j][i-1][2], parent[parent[j][i-1][0]][i-1][2])

for _ in range(int(input())):
    d, e = map(int,input().split())
    print(*lca(d, e))


###### 익혀야할 다른 풀이
import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dp = [[0] * (n + 1)]
min_dp = [[sys.maxsize] * (n + 1)]
max_dp = [[0] * (n + 1)]
queue = deque([(1, 1)])
depth = [0] * (n + 1)
depth[1] = 1
while queue:
    i, d = queue.popleft()
    for j, c in graph[i]:
        if not depth[j]:
            dp[0][j] = i
            min_dp[0][j] = c
            max_dp[0][j] = c
            depth[j] = d + 1
            queue.append((j, d + 1))

k = int(math.log2(max(depth) - 1))
for i in range(1, k + 1):
    temp = [0] * (n + 1)
    min_temp = [sys.maxsize] * (n + 1)
    max_temp = [0] * (n + 1)
    for j in range(1, n + 1):
        a = dp[-1][j]
        temp[j] = dp[-1][a]
        min_temp[j] = min(min_dp[-1][j], min_dp[-1][a])
        max_temp[j] = max(max_dp[-1][j], max_dp[-1][a])
    dp.append(temp)
    min_dp.append(min_temp)
    max_dp.append(max_temp)

for _ in range(int(input())):
    d, e = map(int, input().split())

    if depth[d] > depth[e]:
        d, e = e, d

    diff = depth[e] - depth[d]
    min_d = min_e = sys.maxsize
    max_d = max_e = 0
    while diff:
        m = int(math.log2(diff))
        min_e = min(min_e, min_dp[m][e])
        max_e = max(max_e, max_dp[m][e])
        e = dp[m][e]
        diff -= 2**m

    if d == e:
        print(min_e, max_e)
        continue

    i = 0
    j = depth[d] - 1
    while i < j:
        m = int(math.log2(j - i))
        td = dp[m][d]
        te = dp[m][e]
        if td == te:
            i = j - 2**m + 1
        else:
            j -= 2**m
            min_d = min(min_d, min_dp[m][d])
            max_d = max(max_d, max_dp[m][d])
            min_e = min(min_e, min_dp[m][e])
            max_e = max(max_e, max_dp[m][e])
            d = td
            e = te

    min_ans = min(min_d, min_e, min_dp[0][d], min_dp[0][e])
    max_ans = max(max_d, max_e, max_dp[0][d], max_dp[0][e])

    print(min_ans, max_ans)