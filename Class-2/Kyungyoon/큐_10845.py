from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
command = [list(input().split()) for _ in range(N)]

dq = deque()
for c in command:
    if c[0] == 'push':
        dq.append(c[1])
    elif c[0] == 'pop':
        print(dq.popleft() if dq else -1)
    elif c[0] == 'size':
        print(len(dq))
    elif c[0] == 'empty':
        print(0 if dq else 1)
    elif c[0] == 'front':
        print(dq[0] if dq else -1)
    elif c[0] == 'back':
        print(dq[-1] if dq else -1)
"""
PyPy3
메모리 : 113956 KB
시간 : 160 ms
"""