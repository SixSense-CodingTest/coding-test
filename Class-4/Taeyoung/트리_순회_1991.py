import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder_result = inorder_result = postorder_result = ""


def inorder(node):
    global inorder_result

    if node == '.':
        return

    inorder(tree[node][0])
    inorder_result += node
    inorder(tree[node][1])


def preorder(node):
    global preorder_result

    if node == '.':
        return

    preorder_result += node
    preorder(tree[node][0])
    preorder(tree[node][1])


def postorder(node):
    global postorder_result

    if node == '.':
        return

    postorder(tree[node][0])
    postorder(tree[node][1])
    postorder_result += node


preorder('A')
inorder('A')
postorder('A')
print(preorder_result)
print(inorder_result)
print(postorder_result)

'''
메모리 : 32412 KB
시간 : 40ms
'''
