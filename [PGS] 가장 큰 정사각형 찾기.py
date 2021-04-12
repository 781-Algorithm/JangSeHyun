# 프로그래머스 - 가장 큰 정사각형 찾기
from math import sqrt

def solution(board):
    n = len(board)
    m = len(board[0])

    dp = [[0] * m for _ in range(n)]
    dp[0] = board[0]
    answer = max(dp[0])

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = board[i][j]
            else:
                if board[i][j]:
                    dp[i][j] = (sqrt(min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])) + 1) ** 2
                    answer = max(answer, dp[i][j])



    return int(answer)
