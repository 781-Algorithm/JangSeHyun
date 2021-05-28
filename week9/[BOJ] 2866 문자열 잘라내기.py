# 2866 문자열 잘라내기
from sys import stdin
input = stdin.readline

r,c = map(int,input().split())
words= []
for i in range(r):
    words.append(list(input().rstrip()))

start, end = 0, r-1

while start <= end:
    flag = True
    word_set = set()
    mid = (start+end)//2

    for i in range(c):
        temp = ""
        for j in range(mid,r):
            temp += words[j][i]
        if temp in word_set:
            end = mid - 1
            flag = False
            break
        word_set.add(temp)

    if flag:
        start = mid + 1

print(start-1)

# 더 간단하다.. 이게 훨씬...
n, m = map(int,input().rstrip().split())
l = [input() for _ in range(n)]
ll = []
for i in range(m):
    ll.append(''.join([l[n-j-1][i] for j in range(n)]))
ll.sort()
ans = 0
for i in range(m-1):
    a,b = ll[i],ll[i+1]
    for j in range(n):
        if a[j]!=b[j]:
            ans = max(ans,j)
            break
print(n-ans-1)