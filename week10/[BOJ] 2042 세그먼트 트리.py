# 2042 - 구간 합 구하기 (세그먼트 트리)
import sys, math
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def init_tree(start,node,end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init_tree(start,node*2,mid)+init_tree(mid+1,node*2+1,end)
    return tree[node]

def find_sum(start,end,node,left,right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return find_sum(start,mid,node*2,left,right)+find_sum(mid+1,end,node*2+1,left,right)

def change_num(start,end,node,idx,diff):
    if idx < start or end < idx:
        return
    tree[node] += diff

    if start != end:
        mid = (start+end)//2
        change_num(start,mid,node*2,idx,diff)
        change_num(mid+1,end,node*2+1,idx,diff)

n, m, k = map(int,input().split())
arr = [0]+[int(input()) for _ in range(n)]
cmd = [list(map(int,input().split())) for _ in range(m+k)]

tree = [0 for _ in range(2**(math.ceil(math.log2(n))+1))]
init_tree(1,1,n)
for i in range(m+k):
    if cmd[i][0] == 1: # 수 바꾸기
        diff = cmd[i][2] - arr[cmd[i][1]]
        arr[cmd[i][1]] = cmd[i][2]
        change_num(1,n,1,cmd[i][1],diff)
    else: # 합 출력하기
        print(find_sum(1,n,1,cmd[i][1],cmd[i][2]))