# 14890 경사로
import sys
input = sys.stdin.readline

def check():
    global answer

    for i in range(n):
        count = 1
        flag = True
        j = 1
        while j < n:
            if graph[i][j] == graph[i][j-1]:
                count += 1
                j += 1
                continue
            elif abs(graph[i][j] - graph[i][j-1]) != 1:
                flag = False
                break
            else:
                if graph[i][j] - graph[i][j-1] == 1:
                    if count >= l:
                        count = 1
                        j += 1
                        continue
                    else:
                        flag = False
                        break
                else:
                    count2 = 0
                    for k in range(j,n):
                        if graph[i][k] == graph[i][j]:
                            count2 += 1
                            if count2 >= l:
                                j = k + 1
                                count = 0
                                break
                            elif k == n-1:
                                flag = False
                                j = 101
                                break
                        else:
                            flag = False
                            j = 101
                            break
        if flag:
            answer += 1

    for i in range(n):
        count = 1
        flag = True
        j = 1
        while j < n:
            if graph[j][i] == graph[j-1][i]:
                count += 1
                j += 1
                continue
            elif abs(graph[j][i] - graph[j-1][i]) != 1:
                flag = False
                break
            else:
                if graph[j][i] - graph[j-1][i] == 1:
                    if count >= l:
                        count = 1
                        j += 1
                        continue
                    else:
                        flag = False
                        break
                else:
                    count2 = 0
                    for k in range(j,n):
                        if graph[k][i] == graph[j][i]:
                            count2 += 1
                            if count2 >= l:
                                last = k
                                j = last + 1
                                count = 0
                                break
                            elif k == n-1:
                                flag = False
                                j = 101
                                break
                        else:
                            flag = False
                            j = 101
                            break
        if flag:
            answer += 1

n, l = map(int,input().split())
answer = 0
graph = [list(map(int,input().split())) for _ in range(n)]
check()
print(answer)