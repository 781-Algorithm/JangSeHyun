# 17435 - 합성함수와 쿼리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

m = int(input())
func = [0] + list(map(int,input().split()))
q = int(input())
f_table = [[0 for _ in range(21)] for __ in range(m+1)]

for i in range(1, m+1):
    f_table[i][0] = func[i]

for i in range(1, 21):
    for j in range(1, m+1):
        f_table[j][i] = f_table[f_table[j][i-1]][i-1]

for _ in range(q):
    n, x = map(int,input().split())
    for i in range(20,-1,-1):
        if n >= (1 << i):
            n -= (1 << i)
            x = f_table[x][i]

        if n == 0:
            break
    print(x)