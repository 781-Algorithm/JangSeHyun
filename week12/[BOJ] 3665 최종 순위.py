# 3665 최종 순위
import sys
from collections import deque
input = sys.stdin.readline

def swap(a,b):

    if b in graph[a]:
        graph[a].remove(b)
        in_degree[b] -= 1
        graph[b].append(a)
        in_degree[a] += 1
    elif a in graph[b]:
        graph[b].remove(a)
        in_degree[a] -= 1
        graph[a].append(b)
        in_degree[b] += 1
    else:
        return False
    return True

def topology_sort():
    count = 0
    answer = []
    q = deque()
    for i in range(1,n+1):
        if not in_degree[i]:
            q.append(i)

    while q:
        cur = q.popleft()
        answer.append(cur)
        count += 1
        for next in graph[cur]:
            in_degree[next] -= 1
            if not in_degree[next]:
                q.append(next)

    if len(answer) != n:
        return False
    return answer

t = int(input())
while t:
    n = int(input())
    ranking = list(map(int,input().split()))
    m = int(input())
    graph = [[] for _ in range(n+1)]
    in_degree = [0 for _ in range(n+1)]

    for i in range(n-1):
        for j in range(i+1, n):
            graph[ranking[i]].append(ranking[j])
            in_degree[ranking[j]] += 1

    for _ in range(m):
        a, b = map(int, input().split())
        swap(a, b)

    answer = topology_sort()
    if answer is False:
        print("IMPOSSIBLE")
    else:
        print(*answer)
    t -= 1