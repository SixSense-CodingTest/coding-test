import sys

M = int(input())
input = sys.stdin.readline

S = [0]*21

for _ in range(M):
    cmd = input().strip().split()
    if cmd[0]=='add':S[int(cmd[1])] = 1  
    elif cmd[0]=='remove': S[int(cmd[1])] = 0
    elif cmd[0]=='check': print(1) if S[int(cmd[1])]==1 else print(0)
    elif cmd[0]=='toggle': 

        if S[int(cmd[1])] == 0:
            S[int(cmd[1])] = 1  
        else: 
            S[int(cmd[1])] = 0

    elif cmd[0]=='all': S = [1]*21
    elif cmd[0]=='empty': S = [0]*21

