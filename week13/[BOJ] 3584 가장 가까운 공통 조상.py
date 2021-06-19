import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def find_root():
    for i in range(1,n+1):
        if is_root[i] == 0:
            return i

def dfs(x, count):
    visited[x] = True
    depth[x] = count
    for i in graph[x]:
        if visited[i]:
            continue
        parent[i][0] = x
        dfs(i, count+1)

def lca(a, b):

    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(20,-1,-1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]
    if a == b:
        return a
    for i in range(20, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

t = int(input())
while t:
    n = int(input())
    is_root = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    depth = [0 for _ in range(n+1)]
    parent = [[0 for _ in range(21)] for __ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int,input().split())
        graph[a].append(b)
        is_root[b] = 1

    dfs(find_root(), 0)
    for i in range(1, 21):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

    x, y = map(int,input().split())
    print(lca(x, y))
    t -= 1