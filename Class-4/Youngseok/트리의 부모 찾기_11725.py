import sys
input = sys.stdin.readline
n = int(input())
l = [set() for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    l[a].add(b)
    l[b].add(a)
t = [1]
v = set(t)
p = [0] * (n+1)
while t:
    x = t.pop()
    while l[x]:
        y = l[x].pop()
        if y in v: continue
        p[y] = x
        t.append(y)
        v.add(y)
print(*p[2:])
# 73188kb
# 364ms

import sys
input = sys.stdin.readline
n = int(input())
l = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
t = [1]
v = set(t)
p = [0] * (n+1)
while t:
    x = t.pop()
    while l[x]:
        y = l[x].pop()
        if y in v: continue
        p[y] = x
        t.append(y)
        v.add(y)
print(*p[2:])
# 56804kb
# 300ms
## set() 이 생각보다 메모리 많이 쓰고 작은 크기인 경우 시간이 오래걸리는듯?

import sys
input = sys.stdin.readline
n = int(input())
l = {i:[] for i in range(n+1)}
for i in range(n-1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
t = [1]
v = set(t)
p = [0] * (n+1)
while t:
    x = t.pop()
    while l[x]:
        y = l[x].pop()
        if y in v: continue
        p[y] = x
        t.append(y)
        v.add(y)
print(*p[2:])
# 64432kb
# 404ms
# 오히려 딕셔너리가 셋보다 메모리를 덜씀 아마 set을 여러번 선언하는게 좀 리소스를 먹는듯?