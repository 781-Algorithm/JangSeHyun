# 10026 적록색약
import sys
sys.setrecursionlimit(int(1e6))
def dfs(x,y,mode=0):
    if mode==0:
        col = graph[x][y]
        visited[x][y] = True
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] or graph[nx][ny]!=col:
                continue
            dfs(nx,ny,mode)
    # 적록 색약인 경우
    else:
        col = graph[x][y]
        visited2[x][y] = True
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited2[nx][ny]:
                continue
            if col == 'R' or col == 'G':
                if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                    dfs(nx,ny,mode)
            else:
                if graph[nx][ny] != col:
                    continue
                dfs(nx,ny,mode)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

visited, visited2 = [ [False for _ in range(n)] for _ in range(n)], [ [False for _ in range(n)] for _ in range(n)]
count1, count2 = 0, 0
dx, dy = [0,0,-1,1], [-1,1,0,0]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            count1+=1
        if not visited2[i][j]:
            dfs(i,j,1)
            count2+=1
print(count1,count2)