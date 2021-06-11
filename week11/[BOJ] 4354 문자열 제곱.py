# 4354 문자열 제곱
from math import gcd
def kmp_table(string, string_l):
    pt,pp = 1, 0
    while pt != string_l:
        if string[pt] == string[pp]:
            pt += 1
            pp += 1
            table[pt] = pp
        elif pp == 0:
            pt += 1
            table[pt] = pp
        else:
            pp = table[pp]
    return

while True:
    s = input()
    if s == ".":
        break
    length = len(s)
    table = [0 for _ in range(length + 1)]
    kmp_table(s, length)

    stand = length
    val = table[stand]

    if val == 0 or val * 2 < stand:
        print(1)
        continue

    while val * 2 > stand:
        stand = val
        val = table[stand]

    if val == 1:
        if s[0] != s[1]:
            print(1)
            continue
    else:
        if gcd(length,table[length]) == 1:
            print(1)
            continue
    print(length//val)

## 다른 풀이 - 오.. 이거 되게 직관적이다

def solution(s):
    result = 0
    len_s = len(s)

    if len(set(s)) == 1:
        return len(s)

    for i in range(1, (len(s) // 2) + 1):
        if len_s % i != 0:
            continue
        multiply = len_s // i
        compare = s[:i] * multiply
        if s == compare:
            result = max(result, multiply)
    if result == 0:
        return 1
    return result

while True:
    s = input()
    if s == ".":
        break
    print(solution(s))