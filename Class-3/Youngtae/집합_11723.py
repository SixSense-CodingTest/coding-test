# 비어있는 공집합 S
import sys

input = sys.stdin.readline
M = int(input())
order_set = set()

for _ in range(M):
    order = input().split()
    if order[0] == 'add':
        if int(order[1]) not in order_set:
            order_set.add(int(order[1]))
        else:
            continue
    elif order[0] == 'remove':
        if int(order[1]) in order_set:
            order_set.remove(int(order[1]))
        else:
            continue
    elif order[0] == 'check':
        if int(order[1]) in order_set:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in order_set:
            order_set.remove(int(order[1]))
        else:
            order_set.add(int(order[1]))
    elif order[0] == 'all':
        order_set = {i for i in range(1,21)}
    elif order[0] == 'empty':
        order_set = set()
