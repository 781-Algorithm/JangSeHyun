# 2263 트리의 순회 // 다시 봐야함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

# 이거 구현하는게 너무 빡세다..
def split_tree(i_s,i_e,p_s,p_e):

    if i_s > i_e or p_s > p_e: return
    root = post[p_e]
    idx = inorder_idx[root]
    left = idx - i_s

    print(root,end=' ')

    split_tree(i_s,idx-1,p_s,left+p_s-1)
    split_tree(idx+1,i_e,p_s+left,p_e-1)


n = int(input())
inorder = list(map(int,input().split()))
post = list(map(int,input().split()))
inorder_idx = [0]*(n+1)
for i in range(n):
    inorder_idx[inorder[i]] = i

split_tree(0,n-1,0,n-1)

## 당연한 말이지만, dfs형식이므로 stack쓰면 훨씬 공간복잡도가 낮다

def solve():
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    inorder_index = [None] * (n + 1)
    for idx, node in enumerate(inorder):
        inorder_index[node] = idx

    print_buf = []
    stack = [(0, len(inorder) - 1, 0, len(postorder) - 1)]
    while stack:
        in_start, in_end, post_start, post_end = stack.pop()
        root_idx = inorder_index[postorder[post_end]]
        in_len = root_idx - 1 - in_start
        print_buf.append(f'{postorder[post_end]}')
        if root_idx + 1 <= in_end:
            stack.append((root_idx + 1, in_end, post_start + in_len + 1, post_end - 1))
        if in_start <= root_idx - 1:
            stack.append((in_start, root_idx - 1, post_start, post_start + in_len))
    print(' '.join(print_buf))

solve()
