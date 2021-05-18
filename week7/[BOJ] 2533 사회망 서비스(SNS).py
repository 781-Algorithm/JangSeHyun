# 2533 - 사회망 서비스(SNS)
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
graph =[ [] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]

def dfs(x):
    visited[x] = True
    dp[x][0] = 0
    dp[x][1] = 1
    for node in graph[x]:
        if visited[node]:
            continue
        dfs(node)
        dp[x][0] += dp[node][1]
        dp[x][1] += min(dp[node][0],dp[node][1])

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(a)
print(min(dp[a]))
