# 13913 - 숨바꼭질 4
from collections import deque
def bfs(x):

    dp[x] = x
    q = deque()
    q.append(x)

    while q:
        now = q.popleft()
        if now == k:
            return
        temp = [now-1, now+1, now*2]

        for i in range(3):
            if temp[i] < 0 or temp[i] > 100000:
                continue
            if dp[temp[i]]!= -1:
                continue
            dp[temp[i]] = now
            q.append(temp[i])


n,k = map(int,input().split())
dp = [-1]*100001

if n >= k:
    print(n-k)
    for i in range(n,k-1,-1):
        print(i, end=' ')

else:
    bfs(n)
    answer = []
    while True:
        answer.append(k)
        if k == n:
            break
        k = dp[k]
    print(len(answer)-1)
    print(*answer[::-1])