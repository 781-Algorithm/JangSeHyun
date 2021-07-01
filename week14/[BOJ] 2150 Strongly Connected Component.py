# 2150 Strongly Connected Component
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            stack.append(i)
            dfs(i)
    stack.append(x)


def reverse_dfs(x):

    visited[x] = True
    temp.append(x)

    for i in rev_graph[x]:
        if not visited[i]:
            reverse_dfs(i)


v, e = map(int,input().split())
graph, rev_graph = [[] for _ in range(v+1)], [[] for _ in range(v+1)]

stack, result = [], []
visited = [False for _ in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

for i in range(1, v+1):
    if not visited[i]:
        dfs(i)

visited = [False for _ in range(v+1)]
while stack:
    temp = []
    top = stack.pop()
    if not visited[top]:
        reverse_dfs(top)
        result.append(sorted(temp)+[-1])

print(len(result))
result.sort(key=lambda x:x[0])
for i in result:
    print(*i)