# 5052 전화번호 목록
from sys import stdin
from collections import Counter
input = stdin.readline

def check_consistency():

    for i in p_book:
        for j in range(1,len(i)):
            if p_book[i[:j]]:
                print("NO")
                return

    print("YES")
    return

t = int(input())

while t:
    n = int(input())
    if n == 1:
        print("YES")
        continue
    book = [input().rstrip() for _ in range(n)]
    p_book = Counter(book)
    check_consistency()
    t -= 1

## 트라이를 이용한 풀이
from sys import stdin
input = stdin.readline

class Trie:
    def __init__(self):
        self.head = {}

    def insert(self,string):
        cur = self.head
        for s in string:
            if s not in cur:
                cur[s] = {}
            cur = cur[s]
        cur[-1] = 1

    def check_cons(self,string):
        cur = self.head
        for s in string[:-1]:
            if s not in cur:
                return True
            else:
                cur = cur[s]
                try:
                    cur[-1]
                except KeyError:
                    continue
                else:
                    return False
        return True

t = int(input())
while t:
    n = int(input())
    trie = Trie()
    book = [input().rstrip() for _ in range(n)]

    for i in book:
        trie.insert(i)

    flag = True

    for i in book:
        if trie.check_cons(i):
            continue
        else:
            print("NO")
            flag = False
            break

    if flag:
        print("YES")

    t -= 1