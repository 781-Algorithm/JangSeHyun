from sys import stdin
input = stdin.readline
arr = list(input().strip())
stack = []
cnt = 0
total = 0

for i in range(len(arr)):

    if arr[i] == "(":
        cnt += 1
        stack.append(cnt)
        continue

    else:
        stack.pop()
        cnt-=1
        if arr[i - 1] == ")":
            total += 1

        else:
            total += cnt

print(total)