import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return

n = int(input())
parent = [i for i in range(n)]
temp, graph, total = [], [], 0

for i in range(n):
    x, y, z = map(int,input().split())
    temp.append([x, y, z, i])

for i in range(3):
    temp.sort(key=lambda x: x[i])
    for j in range(1,n):
        graph.append([abs(temp[j-1][i]-temp[j][i]),temp[j-1][3],temp[j][3]])

graph.sort(key=lambda x:x[0])

for dist,x,y in graph:
    if find_parent(x) != find_parent(y):
        union_parent(x,y)
        total+=dist

print(total)