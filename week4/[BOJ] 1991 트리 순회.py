# 1991 트리 순회
def preorder_traverse(node):
    print(node.value,end='')
    preorder_traverse(nodes[node.left]) if node.left != '.' else ''
    preorder_traverse(nodes[node.right]) if node.right != '.' else ''

def inorder_traverse(node):
    inorder_traverse(nodes[node.left]) if node.left != '.' else ''
    print(node.value,end='')
    inorder_traverse(nodes[node.right]) if node.right != '.' else ''

def postorder_traverse(node):
    postorder_traverse(nodes[node.left]) if node.left != '.' else ''
    postorder_traverse(nodes[node.right]) if node.right != '.' else ''
    print(node.value,end='')

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

n = int(input())
nodes = {}

for _ in range(n):
    node,left,right = input().split()
    nodes[node] = Node(node,left,right)

preorder_traverse(nodes['A'])
print()
inorder_traverse(nodes['A'])
print()
postorder_traverse(nodes['A'])
