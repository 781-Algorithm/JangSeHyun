# 12851 - 숨바꼭질 2
from collections import deque

def bfs(x):

    result = 1e9
    count = 0
    q = deque()
    q.append([0,x])
    dp[x] = 0

    while q:

        cnt, now = q.popleft()

        if cnt >= result:
            return result,count

        temp = [now-1,now+1,now*2]

        for i in temp:

            if i < 0 or i > 100000:
                continue

            if dp[i] < cnt:
                continue

            if i == k:
                result = cnt + 1
                count += 1
                q.append([cnt+1,i])
                continue

            if dp[i] >= cnt+1:
                dp[i] = cnt+1
                q.append([cnt+1,i])


n, k = map(int,input().split())
dp = [1e9]*100001


if n >= k:
    print(n-k)
    print(1)

else:
    result, count = bfs(n)
    print(result)
    print(count)
