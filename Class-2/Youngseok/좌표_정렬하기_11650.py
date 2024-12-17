import sys
input = sys.stdin.readline
n = int(input())
p = [input() for _ in range(n)]
p.sort(key = lambda x: tuple(map(int, x.split())))
print(''.join(p))
# 55144 kb
# 216 ms

import sys
input = sys.stdin.readline
n = int(input())
p = sorted([input() for _ in range(n)], key = lambda x: tuple(map(int, x.split())))
print(''.join(p))
# 55144 kb
# 208 ms

import sys
input = sys.stdin.readline
n = int(input())
p = sorted([input() for _ in range(n)])
p.sort(key = lambda x: tuple(map(int, x.split())))
print(''.join(p))
# 53432 kb
# 176 ms
# WHY???????