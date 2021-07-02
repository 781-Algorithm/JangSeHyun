# 4196 도미노 -- 와.. 어렵다..
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
    stack.append(x)

def rev_dfs(x):
    visited[x] = True
    group[x] = count

    for i in rev_graph[x]:
        if not visited[i]:
            rev_dfs(i)

t = int(input())
while t:
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    rev_graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for _ in range(m):
        x, y = map(int,input().split())
        graph[x].append(y)
        rev_graph[y].append(x)

    stack = []
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    visited = [False] * (n + 1)
    group, count = [0]*(n+1), 1
    while stack:
        top = stack.pop()
        if not visited[top]:
            group[top] = count
            rev_dfs(top)
            count += 1

    in_degree = [0]*count
    for i in range(1,n+1):
        for j in graph[i]:
            if group[i] != group[j]:
                in_degree[group[j]] += 1

    answer = 0
    for i in range(1, count):
        if in_degree[i] == 0:
            answer += 1

    print(answer)
    t -= 1