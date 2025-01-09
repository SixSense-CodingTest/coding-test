############
# silver 1 #
############

import sys
from collections import deque

class Node:
    def __init__(self, curr, left=None, right=None):
        self.curr = curr
        self.left = left
        self.right = right

def preorder(node):
    if node:
        print(node.curr, end="")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.curr, end="")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.curr, end="")


input = sys.stdin.readline

number_of_items = int(input())
tree = {}

for _ in range(number_of_items):
    target, left, right = input().split()

    if target not in tree:
        tree[target] = Node(curr=target)

    if left != ".": 
        if left not in tree:
            tree[left] = Node(curr=left)
        tree[target].left = tree[left]

    if right != ".": 
        if right not in tree:
            tree[right] = Node(curr=right)

        tree[target].right = tree[right]

root = tree['A']

preorder(root)
print()
inorder(root)
print()
postorder(root)

###################
# memory: 34992KB #
# time:   56ms    #
###################