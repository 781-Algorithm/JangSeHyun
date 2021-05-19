# 1949 우수 마을
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    dp[x][0] = 0
    dp[x][1] = populations[x]

    for node in graph[x]:
        if visited[node]:
            continue
        dfs(node)
        dp[x][1] += dp[node][0]
        dp[x][0] += max(dp[node][0],dp[node][1])

n = int(input())
populations = [0]+list(map(int,input().split()))
graph, visited = [[]for _ in range(n+1)], [False for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(max(dp[1]))