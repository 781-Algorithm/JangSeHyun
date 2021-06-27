# 3055 탈출
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append((x, y, 0))
    visited = [[False for _ in range(c)] for __ in range(r)]
    visited[x][y] = True
    while q:
        cur_x, cur_y, count = q.popleft()

        if graph[cur_x][cur_y] == "D":
            print(count)
            return

        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:
                continue
            if graph[new_x][new_y] == "X":
                continue
            if visited[new_x][new_y]:
                continue
            if graph[new_x][new_y] in [".", "D"] or graph[new_x][new_y] > count+1:
                visited[new_x][new_y] = True
                q.append((new_x,new_y,count+1))

    print("KAKTUS")
    return

def flow(w):
    q = deque()
    for x, y in w:
        q.append((x, y, 0))
        graph[x][y] = 0
    while q:
        cur_x, cur_y, count = q.popleft()
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c:
                continue
            if graph[new_x][new_y] == "S" or graph[new_x][new_y] == ".":
                graph[new_x][new_y] = count + 1
                q.append((new_x, new_y, count+1))


r, c = map(int,input().split())
water = []
dx, dy = [-1,1,0,0], [0,0,-1,1]
graph = []
for i in range(r):
    row = list(input().rstrip())
    for j in range(c):
        if row[j] == "S":
            start = [i, j]
        elif row[j] == "*":
            water.append([i, j])
    graph.append(row)

flow(water)
bfs(*start)