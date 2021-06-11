import sys
input = sys.stdin.readline

def kmp_table(pattern,text):
    answer, point = 0, []
    pt = 1
    pp = 0
    f_table = [0 for _ in range(pattern_length+1)]

    while pt != pattern_length:
        if pattern[pt] == pattern[pp]:
            pt, pp = pt+1, pp+1
            f_table[pt] = pp
        elif pp == 0:
            pt += 1
            f_table[pt] = pp
        else:
            pp = f_table[pp]

    pt = pp = 0
    while pt != text_length:
        if text[pt] == pattern[pp]:
            pt, pp = pt+1, pp+1
            if pp == pattern_length:
                answer += 1
                point.append(pt-pp+1)
                pp = f_table[pp]

        elif pp == 0:
            pt += 1
        else:
            pp = f_table[pp]

    print(answer)
    if answer == 0:
        point = []
    print(*point)
    return

t = input().rstrip()
p = input().rstrip()
text_length, pattern_length = len(t), len(p)
if text_length >= pattern_length:
    kmp_table(p,t)
else:
    print(0)