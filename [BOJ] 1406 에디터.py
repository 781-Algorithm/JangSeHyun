# 1406 - 에디터
from sys import stdin
input = stdin.readline

string = list(input().strip()) # 앞 스택
temp_stack=[] # 뒤 스택

m = int(input())
cmd = [input().strip() for _ in range(m)]

length = len(string)
cur = length

for i in range(m):

    if cmd[i][0]=="L":
        if cur !=0:
            temp_stack.append(string.pop())
            cur-=1

    elif cmd[i][0]=="D":
        if cur != length:
            string.append(temp_stack.pop())
            cur+=1

    elif cmd[i][0]=="B":
        if cur != 0:
            string.pop()
            cur-=1
            length-=1

    else:
        string.append(cmd[i][-1])
        cur+=1
        length+=1

print(''.join(string+temp_stack[::-1]))