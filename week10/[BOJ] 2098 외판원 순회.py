import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (1 << n - 1) for _ in range(n)]

def solution(i, route):
    
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (n - 1)) - 1:
        if graph[i][0]:
            return graph[i][0]
        else:
            return 1e9

    min_dist = 1e9
    
    for j in range(1, n):
        if not graph[i][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = graph[i][j] + solution(j, route | (1 << (j - 1)))
        if min_dist > dist:
            min_dist = dist
    dp[i][route] = min_dist

    return min_dist


print(solution(0, 0))