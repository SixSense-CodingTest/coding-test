from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

queue = deque()
for _ in range(N):
    cmd = input().strip().split()
    
    if cmd[0]=='push': queue.append(int(cmd[1]))
    elif cmd[0]=='pop': print(queue.popleft()) if len(queue)!=0 else print(-1)
    elif cmd[0]=='size': print(len(queue))
    elif cmd[0]=='empty': print(0) if len(queue)!=0 else print(1)
    elif cmd[0]=='front': print(queue[0]) if len(queue)!=0 else print(-1)
    elif cmd[0]=='back':print(queue[-1]) if len(queue)!=0 else print(-1)
