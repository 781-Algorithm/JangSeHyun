# 1987 알파벳
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))

def dfs(x,y,num):
    global answer

    if num > answer:
        answer = num

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny>=m:
            continue
        if visited[graph[nx][ny]]:
            continue
        visited[graph[nx][ny]] = 1
        dfs(nx,ny,num+1)
        visited[graph[nx][ny]] = 0

    return

graph = []
answer = 1
n,m = map(int,input().split())
dx, dy = [1,-1,0,0], [0,0,-1,1]
visited = [0 for _ in range(26)]
graph = [list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(n)]
visited[graph[0][0]] = 1
dfs(0,0,1)
print(answer)

# 내가 구현해본 bfs
import sys
input = sys.stdin.readline

def bfs(x,y,num):

    global answer
    q = set([(x, y, graph[x][y], num)])

    while q:
        x, y, road, num = q.pop()
        if num > answer:
            answer = num

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] in road:
                continue
            q.add((nx, ny, road + graph[nx][ny],num+1))

    return

graph = []
answer = 1
n,m = map(int,input().split())
dx, dy = [1,-1,0,0], [0,0,-1,1]
for _ in range(n):
    graph.append(list(input().rstrip()))
bfs(0,0,1)
print(answer)