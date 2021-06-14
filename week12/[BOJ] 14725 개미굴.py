# 14725 개미굴 (트라이 자료구조)
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

    def print_trie(self, count, cur):

        try:
            cur[-1]
        except KeyError:
            pass
        else:
            return

        cur_list = sorted(cur)

        for child in cur_list:
            print("--"*count + child)
            self.print_trie(count+1, cur[child])

n = int(input())
trie = Trie()
for _ in range(n):
    num, *string = input().rstrip().split()
    trie.insert(string)

trie.print_trie(0, trie.head)