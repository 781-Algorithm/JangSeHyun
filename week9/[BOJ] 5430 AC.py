# 5430 AC
from sys import stdin
input = stdin.readline

t = int(input())
def AC(n,cmd):
    left = 0
    right = n
    flag = True
    for i in cmd:
        if i == "R":
            flag = not flag
        elif i == "D":
            if flag:
                left += 1
            else:
                right -= 1
            if left > right:
                flag = "error"
                break

    return flag, left, right

while t:
    cmd = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    flag, left, right = AC(n,cmd)

    if flag == "error":
        print("error")
    else:
        print("[",end='')
        arr = arr[left:right]
        if not flag:
            arr.reverse()
        print(",".join(arr),end='')
        print("]")

    t-=1