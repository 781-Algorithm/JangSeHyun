# 17472 - 다리 만들기 2
from collections import deque, defaultdict
from sys import stdin
input = stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def bfs(x, y, cnt):
    q = deque()
    q.append([x,y])
    graph[x][y] = cnt
    while q:
        x, y = q.popleft()
        points[cnt].add((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == cnt or graph[nx][ny] == 0:
                continue
            graph[nx][ny] = cnt
            q.append([nx, ny])
    return

n, m = map(int, input().split())
graph, points = [], defaultdict(set)
cnt = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(lambda x: -int(x), input().split())))

# 그래프 초기화(섬 넘버링)
for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            cnt += 1
            bfs(i, j, cnt)

# cnt가 섬의 개수가 되는 것. 1번부터 시작
parent = [i for i in range(cnt + 1)]
kruskal = []

for i in range(1,cnt+1):
    for point in points[i]:
        x,y = point[0], point[1]

        # 위부분 탐색(같은 열)
        for a in range(x-1,-1,-1):
            if graph[a][y] == i:
                break
            elif graph[a][y] != 0 and graph[a][y] != i:
                dist = x-a-1
                if dist >= 2:
                    kruskal.append([dist,i,graph[a][y]])
                break
        # 아래 부분 탐색 (같은 열)
        for a in range(x+1,n):
            if graph[a][y] == i:
                break
            elif graph[a][y] != 0 and graph[a][y] != i:
                dist = a-x-1
                if dist>= 2:
                    kruskal.append([dist,i,graph[a][y]])
                break

        # 왼쪽 탐색 (같은 행)
        for b in range(y-1,-1,-1):
            if graph[x][b] == i:
                break
            elif graph[x][b] != 0 and graph[x][b] != i:
                dist=y-b-1
                if dist >= 2:
                    kruskal.append([dist,i,graph[x][b]])
                break
        # 오른쪽 탐색
        for b in range(y+1,m):
            if graph[x][b] == i:
                break
            elif graph[x][b] != 0 and graph[x][b] != i:
                dist=y-b-1
                if dist >= 2:
                    kruskal.append([dist,i,graph[x][b]])
                break
kruskal.sort()
total = 0
for dist,start,end in kruskal:
    if find_parent(start)!=find_parent(end):
        union_parent(start,end)
        total+=dist

k = find_parent(1)
flag = True
for i in range(1,cnt+1):
    if find_parent(i)!=k:
        print(-1)
        flag = False
        break

if flag:
    print(total)