# 1759 - 암호 만들기
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def dfs(temp,consonant,vowel,n):

    if n == l:
        if consonant >=2 and vowel >=1:
            result.append(temp)
            return

    for i in range(len(char)):

        if visited[i]:
            continue

        if temp and temp[-1] > char[i]:
            continue

        if char[i] in ['a','e','i','o','u']:
            visited[i] = True
            dfs(temp+[char[i]],consonant,vowel+1,n+1)
            visited[i] = False
        else:
            visited[i] = True
            dfs(temp+[char[i]],consonant+1,vowel,n+1)
            visited[i] = False

l,c = map(int,input().split())
char = list(input().rstrip().split())
visited = [False for _ in range(c)]
result = []
dfs([],0,0,0)
result.sort()
for i in result:
    print("".join(i))