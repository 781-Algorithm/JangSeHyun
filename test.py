import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,visited,start):

    queue = deque()
    visited[0][0][0] = 1
    queue.append(start)

    while queue:

        x,y,c = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny][c]:
                continue

            if graph[nx][ny] == 1 and c == 1:
                continue

            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][c+1] = visited[x][y][c]+1
                queue.append([nx,ny,c+1])

            elif graph[nx][ny] == 0:
                visited[nx][ny][c] = visited[x][y][c]+1
                queue.append([nx,ny,c])

    return visited[-1][-1]

n,m = map(int,input().split())
graph = []
visited = [[[0]*2 for _ in range(m)] for __ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,input().strip())))

a1,a2 = bfs(graph,visited,[0,0,0])

if a1 == 0 and a2==0:
    print(-1)
elif a1 == 0 and a2 !=0:
    print(a2)
else:
    print(min(a1,a2))