# 11723 - 집합 (비트마스크)
import sys
m = int(sys.stdin.readline())
S = 0b0
all_S = 0b111111111111111111111
not_S = 0b000000000000000000000

for i in range(m):
    cmd = sys.stdin.readline().rstrip().split(" ")
    if cmd[0] == "add":
        S = S | (1 << int(cmd[-1]))
    elif cmd[0] == "remove":
        S = S & ~(1 << int(cmd[-1]))
    elif cmd[0] == "check":
        if S & (1 << int(cmd[-1])):
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        S = S ^ (1 << int(cmd[-1]))

    elif cmd[0] == "all":
        S = S | all_S
    else:
        S = S & not_S