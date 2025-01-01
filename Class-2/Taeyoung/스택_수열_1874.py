import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())

num_list = [int(input().rstrip()) for _ in range(N)]
num_deque = deque(num_list)

stack = []
result = []
sign = []

cnt = 1
while cnt <= N:
    sign.append("+")
    stack.append(cnt)

    while True:
        if len(stack) > 0 and stack[-1] == num_deque[0]:
            sign.append("-")
            result.append(stack.pop())
            num_deque.popleft()
        else:
            break

    cnt += 1

if num_list == result:
    print("\n".join(sign))
else:
    print("NO")

'''
메모리 : 43468 KB
시간 : 160 ms
'''
