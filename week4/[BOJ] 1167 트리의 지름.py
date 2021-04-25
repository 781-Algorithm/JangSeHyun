# 1167 - 트리의 지름 // 2번을 왜 하는지에 대한 의미
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x,cost):

    global distance

    for node,dist in tree[x].items():
        if distance[node]!=-1:
            continue
        distance[node] = cost+dist
        dfs(node,cost+dist)

    return

v = int(input())
tree = [{} for _ in range(v+1)]

for i in range(v):
    temp = list(map(int,input().split()))[:-1]
    for j in range(1,len(temp),2):
        tree[temp[0]][temp[j]] = temp[j+1]

distance = [-1]*(v+1)
distance[1] = 0
maxi_idx,maxi = 0,0
dfs(1,0)

for idx,dist in enumerate(distance):
    if maxi < dist:
        maxi = dist
        maxi_idx = idx

distance = [-1]*(v+1)
distance[maxi_idx] = 0
dfs(maxi_idx,0)
print(max(distance))