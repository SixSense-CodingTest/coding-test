def search(node, order, res):
    t = [node] + tree[node]
    t = [t[order[0]],t[order[1]],t[order[2]]]
    for i in t:
        if i == node: res.append(i)
        elif i != '.': search(i, order, res)
    return res
tree = {}
for _ in range(int(input())):
    parent, left, right = input().split()
    tree[parent] = [left, right]
print(''.join(search('A', (0,1,2), [])))
print(''.join(search('A', (1,0,2), [])))
print(''.join(search('A', (1,2,0), [])))
# 32412kb
# 36ms