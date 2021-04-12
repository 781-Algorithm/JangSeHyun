# 13549 - 숨바꼭질 3 힙써서 구현했음.
from heapq import heappop,heappush
n,k = map(int,input().split())
visited = [1e9]*100001

def bfs(x):

    visited[x] = 0
    q = []
    heappush(q,[0,x])

    while q:

        time, now = heappop(q)

        if now == k:
            return time

        temp = [now-1,now+1,now*2]

        for i in range(3):

            if temp[i] < 0 or temp[i] > 100000:
                continue

            if i < 2:
                if visited[temp[i]] <= time+1:
                    continue
                visited[temp[i]] = time+1
                heappush(q,[time+1,temp[i]])

            else:
                if visited[temp[i]] <= time:
                    continue
                visited[temp[i]] = time
                heappush(q,[time,temp[i]])

if n>=k:
    print(n-k)
else:
    print(bfs(n))