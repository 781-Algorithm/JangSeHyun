# 4386 - 별자리 만들기
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

n = int(input())
parent = [i for i in range(n)]
temp, graph = [], []
total = 0
for i in range(n):
    a,b = map(float,input().split())
    temp.append([a,b])
    for j in range(i):
        graph.append([euclid(temp[j],[a,b]),j,i])
graph.sort()
for road in graph:
    dist, a, b = road
    if find_parent(a)!=find_parent(b):
        total+=dist
        union_parent(a,b)
print(total)