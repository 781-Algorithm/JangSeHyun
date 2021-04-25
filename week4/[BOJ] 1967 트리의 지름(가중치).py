# 1967 - 트리의 지름 (가중치)
import sys
from collections import defaultdict as ddict
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

def dfs(x,dist):
    if not tree[x]:
        return
    for node,cost in tree[x]:
        if distance[node] != -1:
            continue
        distance[node] = dist+cost
        dfs(node,dist+cost)
    return

n = int(input())
tree = ddict(list)
distance = {}
maxi_idx, maxi = 0, 0
for i in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
for i in tree.keys():
    distance[i] = -1
distance[1] = 0
dfs(1,0)
for node,dist in distance.items():
    if maxi < dist:
        maxi = dist
        maxi_idx = node
    distance[node] = -1
distance[maxi_idx] = 0
dfs(maxi_idx,0)

if n==1:
    print(0)
else:
    result = 0
    for temp in distance.values():
        result = max(result,temp)
    print(result)