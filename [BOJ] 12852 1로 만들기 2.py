# 12852 - 1로 만들기 2 // 못풀었음. 아이디어를 알고는 있었지만 구현이 될까 싶었는데..
n = int(input())
dp = [[0,[]] for _ in range(n+1)]

for i in range(2,n+1):
    dp[i][0] = dp[i-1][0]+1
    dp[i][1] = dp[i-1][1]+[i-1]

    if i%2 == 0 and dp[i//2][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//2][0]+1
        dp[i][1] = dp[i//2][1]+[i//2]

    if i%3 == 0 and dp[i//3][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i//3]

dp[n][1].append(n)
result = dp[n][0]
result_arr = dp[n][1]
print(result)
print(*result_arr[::-1])

# 근데 이방법은 시/공간 복잡도 엄청 잡아먹는다. 일반적인 풀이 방법은 될 수 있지만, 최적해는 아님
# 필요없는 것들도 path를 다 들고오기 때문에 시간 + 공간 잡아먹는건 당연.
# 다른 효율적인 방법을 찾아봤는데.. https://www.acmicpc.net/source/27339945 참조
# 다른점이 뭘까... 원래 시도한 방법은 바텀업이었지만 여기서는 탑다운 방식으로 전개함.
# 그리고 불러올때는 바텀업으로 가져온다. 이게 문제가 원하던 방향 아니었을까...

n = int(input())
# 6 -> 2 -> 1
way = {n:-1}

def topdown(n):
    stack = [n]

    for temp in stack:

        if temp == 1:
            break

        temp_stack = [temp-1]

        if temp%2 == 0:
            temp_stack.append(temp//2)
        if temp%3 == 0:
            temp_stack.append(temp//3)

        for temp2 in temp_stack:
            if temp2 not in way:
                stack.append(temp2)
                way[temp2] = temp

topdown(n)
result = []
start = 1
while True:
    result.append(start)
    if start == n:
        break
    start = way[start]

print(len(result)-1)
print(*result[::-1])