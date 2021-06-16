# 5670 휴대폰 자판
from sys import stdin
input = stdin.readline

class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, string):
        cur = self.head
        for s in string:
            if s not in cur:
                cur[s] = {}
                try:
                    cur['COUNT']
                except KeyError:
                    cur['COUNT'] = 1
                else:
                    cur['COUNT'] += 1
            cur = cur[s]
        cur[-1] = True

    def button_count(self, cur, count):

        global total

        try:
            cur[-1]
        except KeyError:
            if cur['COUNT'] == 1:
                for key in cur:
                    if key in ['COUNT', -1]:
                        continue
                    if cur == self.head:
                        count += 1
                    self.button_count(cur[key], count)
            else:
                for key in cur:
                    if key in ['COUNT', -1]:
                        continue
                    self.button_count(cur[key], count + 1)
        else:
            try:
                cur['COUNT']
            except KeyError:
                # 리프노드
                total += count
                pass
            else:
                # 리프노드가 아님
                total += count
                for key in cur:
                    if key in ['COUNT', -1]:
                        continue
                    self.button_count(cur[key], count + 1)
        return
while True:
    try:
        n = int(input().rstrip())
        trie = Trie()
        total = 0
        for _ in range(n):
            trie.insert(input().rstrip())
        trie.button_count(trie.head, 0)
        print("{:.2f}".format(round(total / n, 2)))

    except:
        break