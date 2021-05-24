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


# bfs
import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)

# 내가 구현해본 bfs (진행중)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,num):
    global answer

    q = deque()
    q.append([x,y,[graph[x][y]],num])

    while q:

        x, y, road, num = q.popleft()

        if num > answer:
            answer = num

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] in road:
                continue
            q.append([nx,ny,road+[graph[nx][ny]],num+1])

    return

graph = []
answer = 1
n,m = map(int,input().split())
dx, dy = [1,-1,0,0], [0,0,-1,1]
for _ in range(n):
    graph.append(list(input().rstrip()))
bfs(0,0,1)
print(answer)