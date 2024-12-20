import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    c = input().strip().split()
    if  c[0] == 'push': s.append(c[1])
    elif c[0] == 'pop': print(s.pop(0) if s else -1) # 입력이 최대 1만 개라 오히려 리스트가 더 빠른듯?
    elif c[0] == 'size': print(len(s))
    elif c[0] == 'empty': print(0 if s else 1)
    elif c[0] == 'front': print(s[0] if s else -1)
    elif c[0] == 'back': print(s[-1] if s else -1)
# 33432kb
# 40ms

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
s = deque()
for i in range(n):
    c = input().strip().split()
    if  c[0] == 'push': s.append(c[1])
    elif c[0] == 'pop': print(s.popleft() if s else -1)
    elif c[0] == 'size': print(len(s))
    elif c[0] == 'empty': print(0 if s else 1)
    elif c[0] == 'front': print(s[0] if s else -1)
    elif c[0] == 'back': print(s[-1] if s else -1)
# 34924kb
# 64ms