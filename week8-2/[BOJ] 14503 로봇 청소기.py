# 14503 로봇 청소기
# 1은 벽 -1 이미 청소 0은 아직 청소 x
import sys
sys.setrecursionlimit(int(1e5))

def dfs(x, y, d, num):
    global result

    if num != 4:
        if graph[x][y]==0:
            graph[x][y] = -1
            result += 1

        nx = x + dx[3-d]
        ny = y + dy[3-d]

        if 0 <= nx < n and 0 <= ny < m:
            if d == 0:
                nd = 3
            else:
                nd = d-1

            if graph[nx][ny]: # 청소가 되었거나 벽이면
                return dfs(x,y,nd,num+1) # 그 방향으로 틀고 스택을 쌓아줌
            else:
                return dfs(nx,ny,nd,0) # 그 방향으로 이동시키고 2를 다시 시행

    else: # 스택이 모두 쌓여있으면 후진해야함
        if d == 0:
            nx, ny = x + 1, y
        elif d == 1:
            nx, ny = x, y - 1
        elif d == 2:
            nx, ny = x-1, y
        else:
            nx, ny = x, y+1

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                return
            else:
                return dfs(nx,ny,d,0)

    return

n, m = map(int,input().split())
r, c, d = map(int,input().split()) # 0 - 북, 1 - 동, 2 - 남, 3 - 서
graph, result = [], 0
dx, dy = [1,0,-1,0], [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

dfs(r,c,d,0)
print(result)
