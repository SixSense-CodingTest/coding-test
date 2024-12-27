import sys
input = sys.stdin.readline
n = int(input())
p = sorted([input() for _ in range(n)], key = lambda x: (int(x.split()[1]), int(x.split()[0])))
print(''.join(p))
# 55144kb
# 188ms

import sys
input = sys.stdin.readline
print(''.join(sorted([input() for _ in range(int(input()))], key = lambda x: (int(x.split()[1]), int(x.split()[0])))))
# 55000kb
# 180ms