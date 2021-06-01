# 11725 - 트리의 부모 찾기
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(x):
    if not tree[x]:
        return
    for con in tree[x]:
        if parent[con]==0:
            parent[con] = x
            dfs(con)

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
parent[1] = 1

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dfs(1)
for i in parent[2:]:
    print(i)