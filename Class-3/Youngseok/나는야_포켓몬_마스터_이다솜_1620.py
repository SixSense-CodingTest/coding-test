import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
d = {}
for i in range(1,n+1):
    p = input().strip()
    d[p], d[f'{i}'] = i, p
for i in range(m):
    q = input().strip()
    print(f'{d[q]}\n')
# 55964kb
# 208ms

import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
d = {}
for i in range(1,n+1): d[p], d[f'{i}'] = i, (p:=input().strip())
for i in range(m): print(f'{d[input().strip()]}\n')
# 55964kb
# 200ms