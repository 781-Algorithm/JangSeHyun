# 1305 광고
import sys
input = sys.stdin.readline

def kmp_table(text,length):

    pt = 1
    pp = 0
    while pt != length:
        if text[pt] == text[pp]:
            pt, pp = pt + 1, pp + 1
            table[pt] = pp
        elif pp == 0:
            pt += 1
        else:
            pp = table[pp]


l = int(input())
text = input().rstrip()
table = [0 for i in range(l+1)]
kmp_table(text,l)
print(l - table[l])