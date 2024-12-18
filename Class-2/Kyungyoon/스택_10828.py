from collections import deque
N = int(input())
command = [list(input().split()) for _ in range(N)]

dq = deque()
for c in command:
    if c[0] == 'push':
        dq.append(c[1])
    if c[0] == 'pop':
        if len(dq) != 0:
            p = dq.pop()
            print(p)
        else:
            print(-1)
    if c[0] == 'size':
        print(len(dq))
    if c[0] == 'empty':
        if len(dq) != 0:
            print(0)
        else:
            print(1)
    if c[0] == 'top':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)

"""
PyPy3
메모리 : 114504 KB
시간 : 156 ms
"""