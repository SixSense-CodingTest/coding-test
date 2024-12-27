import sys
input = sys.stdin.readline
n = int(input())
t = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
res = [t[0]]
for i in range(1,n):
    if res[-1][1] <= t[i][0]: res.append(t[i])
print(len(res))
# 55000kb
# 244ms

import sys
input = sys.stdin.readline
n = int(input())
t = [tuple(map(int, input().split())) for _ in range(n)]
t.sort(key=lambda x: (x[1], x[0]))
res = [t[0]]
for i in range(1,n):
    if res[-1][1] <= t[i][0]: res.append(t[i])
print(len(res))
# 54216kb
# 240ms

import sys
input = sys.stdin.readline
n = int(input())
t = [tuple(map(int, input().split())) for _ in range(n)]
t.sort(key=lambda x: x[0])
t.sort(key=lambda x: x[1])
res = [t[0]]
for i in range(1,n):
    if res[-1][1] <= t[i][0]: res.append(t[i])
print(len(res))
# 48072kb
# 224ms

import sys
input = sys.stdin.readline
n = int(input())
t = [tuple(map(int, input().split())) for _ in range(n)]
t.sort(key=lambda x: x[0])
t.sort(key=lambda x: x[1])
res = [t[0]]
for i in range(1,n):
    if res[-1][1] > t[i][0]: continue
    res.append(t[i])
print(len(res))
# 48072kb
# 208ms
