# 9019 - DSLR // 야 이거 문자열로는 죽어도 안되나 보다.. python으로도..
# 이거 왜 자꾸 시간초과나냐 미치겠네
# pypy3로 하면 통과
from collections import deque, defaultdict

def rotate(x, direction):

    x1 = x // 1000  # 1000 자리
    x2 = (x % 1000) // 100  # 100 자리
    x3 = (x % 100) // 10  # 10 자리
    x4 = x % 10

    if direction == 0:
        return x2*1000+x3*100+x4*10+x1
    else:
        return x4*1000+x1*100+x2*10+x3

def bfs(a, b):

    dp[a] = ['start', a]
    q = deque()
    q.append(a)

    while q:

        now = q.popleft()
        temp = [(2 * now) % 10000, now - 1 if now != 0 else 9999,
                rotate(now, 0), rotate(now, 1)]
        for i in range(4):

            if dp[temp[i]]:
                continue

            dp[temp[i]]=[cmd[i],now]
            q.append(temp[i])

            if temp[i] == b:
                return
    return

t = int(input())
cmd = ["D", "S", "L", "R"]

while t:
    a, b = map(int, input().split())
    dp = defaultdict(list)
    bfs(a,b)
    result = []
    while True:
        result.append(dp[b][0])
        if dp[b][1] == a:
            break
        b = dp[b][1]
    print(*result[::-1],sep='')

    t -= 1