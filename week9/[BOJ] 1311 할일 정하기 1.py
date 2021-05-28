# 1311 할일 정하기 1 (pypy3)
graph = {}

def bit_counting(x): # 몇명이 작업에 투입되었는지? --> 비트에 포함된 1의 개수 세기
    answer = 0
    while x:
        answer += (x & 1)
        x >>= 1
    return answer

n = int(input())
dp = [1e9]*(1<<n)
for i in range(n):
    graph[i] = list(map(int,input().split()))

dp[0] = 0
for i in range(1<<n):
    k = bit_counting(i)
    for j in range(n):
        if not i & (1 << j):
            dp[i | 1 << j] = min(dp[i | 1 << j], dp[i]+graph[k][j])

print(dp[-1])