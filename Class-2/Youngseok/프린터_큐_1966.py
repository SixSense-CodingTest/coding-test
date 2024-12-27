import sys
from collections import deque
input = sys.stdin.readline
for i in range(int(input())):
    m = int(input().split()[1])+1
    q = deque(map(int, input().split()))
    r = 1
    while m:=(m-1-q.index(max(q)))%len(q): 
        q.rotate(-q.index(max(q)))
        q.popleft()
        r += 1
    print(r)
# 34924kb
# 56ms