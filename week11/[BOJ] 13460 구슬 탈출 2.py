# 13460 - 구슬 탈출 2
import sys
from collections import deque
input = sys.stdin.readline

def bfs(r_x, r_y, b_x, b_y):

    q = deque()
    q.append([r_x, r_y, b_x, b_y, 0])

    while q:

        red_x, red_y, blue_x, blue_y, count = q.popleft()

        if count <= 9:

            for i in range(4):

                flag = False
                n_red_x, n_red_y = red_x, red_y
                n_blue_x, n_blue_y = blue_x, blue_y

                while graph[n_blue_x+dx[i]][n_blue_y+dy[i]] != "#":
                    n_blue_x += dx[i]
                    n_blue_y += dy[i]
                    if [n_blue_x, n_blue_y] == goal:
                        flag = True

                while graph[n_red_x+dx[i]][n_red_y+dy[i]] != "#":

                    n_red_x += dx[i]
                    n_red_y += dy[i]

                    if [n_red_x, n_red_y] == goal:
                        if not flag:
                            return count+1

                if n_red_x == n_blue_x and n_red_y == n_blue_y:
                    if i == 0:
                        if blue_x > red_x:
                            n_red_x -= 1
                        else:
                            n_blue_x -= 1
                    elif i == 1:
                        if blue_x < red_x:
                            n_red_x += 1
                        else:
                            n_blue_x += 1
                    elif i == 2:
                        if red_y < blue_y:
                            n_blue_y += 1
                        else:
                            n_red_y += 1
                    else:
                        if red_y > blue_y:
                            n_blue_y -= 1
                        else:
                            n_red_y -= 1

                if flag:
                    continue
                if [red_x,red_y,blue_x,blue_y] == [n_red_x,n_red_y,n_blue_x,n_blue_y]:
                    continue
                q.append([n_red_x,n_red_y,n_blue_x,n_blue_y,count+1])
    return -1


n, m = map(int,input().split())
graph, dx, dy = [], [1,-1,0,0], [0,0,-1,1]
red, blue, goal = [], [], []
for i in range(n):
    l = list(input().rstrip())
    for j in range(m):
        if l[j] == "R":
            red = [i, j]
        elif l[j] == "B":
            blue = [i, j]
        elif l[j] == "O":
            goal = [i, j]
    graph.append(l)

print(bfs(*red, *blue))