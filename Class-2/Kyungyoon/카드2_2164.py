from collections import deque
N = int(input())
dq = deque()
for i in range(N):
    dq.append(i+1)

while len(dq) > 1:
    dq.popleft()
    N = dq.popleft()
    dq.append(N)

print(dq.pop())

"""
PyPy3
메모리 : 126320 KB
시간 : 140 ms
"""