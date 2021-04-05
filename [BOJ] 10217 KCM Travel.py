# 10217 - KCM Travel
from sys import stdin
input = stdin.readline
INF = 1e9
t = int(input())

while t:
    n, m, k = map(int, input().split())
    graph = [ [] for _ in range(n+1)]
    dp = [[INF]*(m+1) for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = map(int,input().split())
        graph[u].append([v,c,d])

    dp[1][0] = 0

    for j in range(m+1):
        for i in range(1,n+1):
            if dp[i][j]!=INF:
                for k in graph[i]:
                    if k[1]+j > m:
                        continue
                    dp[k[0]][k[1]+j] = min(dp[k[0]][k[1]+j],dp[i][j]+k[2])
    result = min(dp[n])
    print("Poor KCM" if result==INF else result)

    t-=1