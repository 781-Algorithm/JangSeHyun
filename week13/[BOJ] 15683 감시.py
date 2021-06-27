# 15683 - 감시
import sys
from collections import deque
input = sys.stdin.readline


def dfs(cnt):
    global answer
    if cnt == cam_num:
        temp = 0
        k = 0
        visited = [[False for _ in range(m)] for __ in range(n)]
        while k != cam_num:
            cam, x, y, direc = q[k]
            ndx, ndy = [], []
            for direction in forward[cam][direc]:
                ndx.append(dx[direction])
                ndy.append(dy[direction])

            for i in range(len(ndx)):
                nx, ny = x, y
                while 0 <= nx + ndx[i] < n and 0 <= ny + ndy[i] < m and graph[nx + ndx[i]][ny + ndy[i]] != 6:
                    nx += ndx[i]
                    ny += ndy[i]
                    if graph[nx][ny] == 0 and not visited[nx][ny]:
                        temp += 1
                        visited[nx][ny] = True
            k += 1
        if num_0 - temp < answer:
            answer = num_0 - temp
        return

    else:
        if camera[cnt][0] == 5:
            for direction in range(1):
                q.append([*camera[cnt], direction])
                dfs(cnt + 1)
                q.pop()

        elif camera[cnt][0] in [1, 3, 4]:
            for direction in range(4):
                q.append([*camera[cnt], direction])
                dfs(cnt + 1)
                q.pop()

        elif camera[cnt][0] == 2:
            for direction in range(2):
                q.append([*camera[cnt], direction])
                dfs(cnt + 1)
                q.pop()

n, m = map(int, input().split())
graph, camera, q = [], [], deque()
cam_num, num_0, answer = 0, 0, 65
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if 1 <= row[j] <= 5:
            camera.append([row[j], i, j])
            cam_num += 1
        elif row[j] == 0:
            num_0 += 1
    graph.append(row)
camera.sort(key=lambda x: x[0], reverse=True)
forward = [[],
           [[0], [1], [2], [3]],
           [[2, 3], [0, 1]],
           [[0, 3], [3, 1], [1, 2], [0, 2]],
           [[2, 0, 3], [1, 2, 3], [0, 1, 3], [0, 1, 2]],
           [[0, 1, 2, 3]]
           ]
dfs(0)
print(answer)