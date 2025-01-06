import sys
input = sys.stdin.readline
n = int(input())
l = [0]
for _ in range(n):
    t = list(map(int, input().split()))
    for i in range(len(t)):
        if i == 0: t[i] = l[i] + t[i]
        elif i == len(t)-1: t[i] = l[i-1] + t[i]
        else: t[i] = max(l[i], l[i-1]) + t[i]
    l = t
print(max(l))
# 32412kb
# 104ms

import sys
input = sys.stdin.readline
n = int(input())
l = [0]
for _ in range(n):
    t = list(map(int, input().split()))
    t[0] += l[0]
    for i in range(1,len(t)-1):
        t[i] += max(l[i], l[i-1])
    t[-1] += l[-1]
    l = t
print(max(l))
# 32412kb
# 80ms
