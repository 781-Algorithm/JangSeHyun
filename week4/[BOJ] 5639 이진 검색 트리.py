# 5639 이진 검색 트리 - 앞 문제와 비교해 보자 뭔가 통하는게 있어야함.
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def post_traverse(start,end):

    if start > end:
        return
    root = pre_order[start]
    bound = start+1

    while bound <= end:
        if root < pre_order[bound]:
            break
        bound+=1 # 이 과정을 bisect_left로 바꿔도 됨. 세번째와 네번째 인자 조절

    post_traverse(start+1,bound-1)
    post_traverse(bound,end)
    print(root) # 후위순회니까 루트를 젤 마지막에 찍는다!


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_traverse(0,len(pre_order)-1)

# bisect_left로 교체했더니 50배 빨라짐... 
import sys
from bisect import bisect_left
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def post_traverse(start,end):

    if start > end:
        return
    root = pre_order[start]
    bound = bisect_left(pre_order,root,start+1,end+1)
    post_traverse(start+1,bound-1)
    post_traverse(bound,end)
    print(root)

pre_order = []

while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_traverse(0,len(pre_order)-1)