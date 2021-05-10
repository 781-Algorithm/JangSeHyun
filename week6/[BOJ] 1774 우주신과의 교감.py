# 1774 - 우주신과의 교감 // 맞긴했는데.. 시간이 왤캐 많이 걸리지? 좀 더 효율적인 방법?
import sys
from math import sqrt
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

def euclid(x,y):
    return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

n,m = map(int,input().split())
graph, temp, parent = [], [], [i for i in range(n+1)]
total = 0

for i in range(n):
    a,b = map(float,input().split())
    temp.append([a,b])
    for j in range(i):
        graph.append([euclid([a,b],temp[j]),j+1,i+1])

graph.sort()

for i in range(m):
    a, b = map(int,input().split())
    union_parent(a,b)

for road in graph:
    dist, a, b = road
    if find_parent(a)!= find_parent(b):
        union_parent(a,b)
        total+=dist

print("{:.2f}".format(total))