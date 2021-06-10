# 2482 - 색상환
n, k = int(input()), int(input())

if k * 2 > n:
    print(0)
else:
    dp = [[0 for _ in range(k+1)] for __ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = i
    for j in range(2,k+1):
        for i in range(2,n+1):
            dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % 1000000003
    if k == 1:
        print(dp[n][k])
    elif k == 2:
        print(dp[n][k] - 1)
    else:
        if dp[n][k] < dp[n-4][k-2]:
            print(dp[n][k]+1000000003-dp[n-4][k-2])
        else:
            print(dp[n][k] - dp[n-4][k-2])