import sys
input = sys.stdin.readline
c, n = int(input()), int(input())
l = {i:set() for i in range(1,c+1)}
for _ in range(n):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)
v, n = {1}, l[1]
while n:
    nn = n.pop()
    if nn in v: continue
    n |= l[nn] 
    v.add(nn)
print(len(v)-1)
# 32412kb
# 36ms

import sys
input = sys.stdin.readline
def dfs(n, g, v):
    v.add(n)
    for i in g[n]:
        if i in v: continue
        v |= dfs(i,g,v)
    return v
c, n = int(input()), int(input())
l = {i:set() for i in range(1,c+1)}
for _ in range(n):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)
print(len(dfs(1, l, set()))-1)
# 32412kb
# 36ms