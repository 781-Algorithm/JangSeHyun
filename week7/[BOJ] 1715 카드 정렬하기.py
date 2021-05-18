# 1715 - 카드 정렬하기
from sys import stdin
from heapq import heappop, heappush, heapify
input = stdin.readline

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

if n == 1:
    print(0)
else:
    heapify(cards)
    stack = []
    while n>1:
        a = heappop(cards)
        b = heappop(cards)
        stack.append(a+b)
        heappush(cards,a+b)
        n-=1

    print(sum(stack))