# 14425 문자열 집합
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
        cur[-1] = True

    def check_string(self, string):
        global answer
        cur = self.head

        for s in string:
            if s not in cur:
                return
            else:
                cur = cur[s]

        try:
            cur[-1]
        except KeyError:
            return
        else:
            answer += 1
        return

n, m = map(int,input().split())
trie = Trie()
answer = 0
for _ in range(n):
    trie.insert(input().rstrip())

for __ in range(m):
    trie.check_string(input().rstrip())

print(answer)