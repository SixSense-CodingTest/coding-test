import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

dq = deque([i for i in range(1, N+1)])
ans = []

while dq:
    # k-1번 왼쪽으로 회전
    dq.rotate(-(K-1))
    ans.append(dq.popleft())

print(f'<{", ".join(map(str, ans))}>')

"""
PyPy3
메모리 : 110064 KB
시간 : 116 ms
"""