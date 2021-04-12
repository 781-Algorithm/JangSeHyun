# 11780 - 플로이드 2
from sys import stdin
input = stdin.readline

def path_find(x,y):
    if path[x][y]==0:
        return []

    k = path[x][y]
    return path_find(x,k)+[k]+path_find(k,y)
# 이 함수가 핵심이다... 아 슈벌... 이거 시간 돼?

def floyd(n):

    for i in range(1,n+1):
        distance[i][i] = 0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1, n+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = k

    return


n = int(input())
m = int(input())
distance = [[1e9]*(n+1) for _ in range(n+1)]
path = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if distance[a][b]==1e9:
        distance[a][b] = c
    else:
        if distance[a][b] > c:
            distance[a][b] = c
floyd(n)

for i in range(1,n+1):
    print(*distance[i][1:])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j]==0 or distance[i][j]==1e9:
            print(0)
        else:
            result = [i]+path_find(i,j)+[j]
            print(len(result),end=' ')
            print(*result)
