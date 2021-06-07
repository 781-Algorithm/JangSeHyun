# 15686 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

def manhattan_dist(start,dest):
    return abs(start[0]-dest[0])+abs(start[1]-dest[1])

def min_dist(h_n,s_n):
    global answer

    for selected in combinations(store, s_n):
        dist = [100 for _ in range(h_n)]
        for s in range(s_n):
            for h in range(h_n):
                dist[h] = min(dist[h], manhattan_dist(house[h], selected[s]))
        answer = min(answer,sum(dist))
    return

n, m = map(int,input().split())
house, store = [], []
answer = 1e9
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append([i,j])
        elif row[j] == 2:
            store.append([i,j])

min_dist(len(house),m)
print(answer)