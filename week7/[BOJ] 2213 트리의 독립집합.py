# 2213 - 트리의 독립집합 // 구현 실패
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

def dfs(x):
    visited[x] = True
    # 초기화 시켜주기
    dp[x][0] = cost[x]
    dp[x][1] = 0
    for node in graph[x]:
        if visited[node]:
            continue
        dfs(node)
        dp[x][0] += dp[node][1] # 본인이 포함되면 아래 노드는 포함 안된 것들만 더해줌
        dp[x][1] += max(dp[node][0],dp[node][1]) # 본인이 포함되지 않으면 아래 노드중 큰값.

def back_tracking(cur, before_status):

    if before_status:
        checked[cur] = False
        for node in graph[cur]:
            if checked[node]==-1:
                back_tracking(node,False)
    else:
        if dp[cur][0] > dp[cur][1]:
            checked[cur] = True
        else:
            checked[cur] = False

        for node in graph[cur]:
            if checked[node]==-1:
                back_tracking(node, checked[cur])

n = int(input())
cost = [0]+list(map(int,input().split()))
graph = [[]for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)] # 서브트리 재귀로 갈건데, 0번째는 본인(루트)가 포함, 1번째는 미포함
visited, checked = [False for _ in range(n+1)], [-1 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(a)
back_tracking(a,False)

result = []
for i in range(1,n+1):
    if checked[i]==True:
        result.append(i)

result.sort()
print(max(dp[a]))
print(*result)