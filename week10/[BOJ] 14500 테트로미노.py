import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x, y, temp, num):
    global answer
    if num == 4:
        if temp > answer:
            answer = temp
            return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            dfs(nx,ny,temp+graph[nx][ny],num+1)
            visited[nx][ny] = False
    return

def check_cross(x,y):

    global answer

    if 0 < x < n-1 and 0 < y < m-1:
        answer = max(answer,
                     graph[x][y] + graph[x][y - 1] + graph[x][y + 1] + graph[x - 1][y],
                     graph[x][y] + graph[x][y - 1] + graph[x][y + 1] + graph[x + 1][y],
                     graph[x][y] + graph[x][y - 1] + graph[x + 1][y] + graph[x - 1][y],
                     graph[x][y] + graph[x][y + 1] + graph[x + 1][y] + graph[x - 1][y])

    elif y == 0 and 0 < x < n-1:
        answer = max(answer
                     ,graph[x][y]+graph[x][y+1]+graph[x+1][y]+graph[x-1][y])

    elif y == m-1 and 0 < x < n-1:
        answer = max(answer,
                     graph[x][y]+graph[x][y-1]+graph[x+1][y]+graph[x-1][y])

    elif x == 0 and 0 < y < m-1:
        answer = max(answer,
                     graph[x][y]+graph[x][y-1]+graph[x][y+1]+graph[x+1][y])

    elif x == n-1 and 0 < y < m-1:
        answer = max(answer,
                     graph[x][y]+graph[x][y-1]+graph[x][y+1]+graph[x-1][y])

    else:
        return


n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,graph[i][j],1)
        check_cross(i,j)
        visited[i][j] = False
print(answer)