# 1717 - 집합의 표현
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    q = find_parent(parent, x)
    w = find_parent(parent, y)
    if q < w:
        parent[w] = q
    else:
        parent[q] = w
    return

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())

    if b == c:
        if a == 0: continue
        else:
            print("YES")
            continue

    if a == 0:
        union_parent(parent, b, c)
    else:
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")