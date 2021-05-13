# 15681 트리와 쿼리
from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def make_tree(cur, root):
    for node in temp[cur]:
        if node!=root:
            graph[cur].append(node)
            parent[node] = cur
            make_tree(node,cur)

def sub_tree(cur):
    count[cur] = 1
    for node in graph[cur]:
        sub_tree(node)
        count[cur] += count[node]


n,r,q = map(int,input().split())
parent, temp = [0 for _ in range(n+1)], [[] for _ in range(n+1)]
graph = defaultdict(list)
count = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    temp[a].append(b)
    temp[b].append(a)

make_tree(r,-1)
sub_tree(r)

for _ in range(q):
    print(count[int(input())])

# 좀 더 익숙한 방법으로 들어가보자.
# 앞선 방법 보다 시간을 0.5로 줄인다.
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for node in temp[x]:
        if visited[node]:
            continue
        dp[x] += dfs(node)
    return dp[x]

n,r,q = map(int,input().split())
temp = [[] for _ in range(n+1)]
visited, dp = [False]*(n+1), [1 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    temp[a].append(b)
    temp[b].append(a)

dfs(r)

for _ in range(q):
    print(dp[int(input())])