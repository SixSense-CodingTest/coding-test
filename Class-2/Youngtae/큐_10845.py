import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
order_list = deque()

for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        order_list.append(order[1])
    elif order[0] =='pop':
        if order_list:
            print(order_list.popleft())
        else:
            print(-1)
    elif order[0] =='size':
        print(len(order_list))
    elif order[0] =='empty':
        if order_list:
            print(0)
        else:
            print(1)
    elif order[0] =='front':
        if order_list:
            print(order_list[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if order_list:
            print(order_list[-1])
        else:
            print(-1)
