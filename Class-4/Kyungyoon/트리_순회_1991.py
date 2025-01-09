class Tree:
    def __init__(self):
        self.tree = {}

    def add(self, root, left, right):
        self.tree[root] = (left, right)

    def pre(self, node):
        if node == '.':
            return ''
        left, right = self.tree[node]
        return node + self.pre(left) + self.pre(right)
    # A + BD. + CE..F.G

    def middle(self, node):
        if node == '.':
            return ''
        left, right = self.tree[node]
        return self.middle(left) + node + self.middle(right)
    # DB. + A + ECFG
 
    def post(self, node):
        if node == '.':
            return ''
        left, right = self.tree[node]
        return self.post(left) + self.post(right) + node
    # D.B + ..E.GFC + A

N = int(input())
tree = Tree()

for _ in range(N):
    root, left, right = input().split()
    tree.add(root, left, right)

print(tree.pre('A'))  
print(tree.middle('A'))   
print(tree.post('A')) 

"""
PyPy3
메모리 : 108384 KB
시간 : 92 ms
"""