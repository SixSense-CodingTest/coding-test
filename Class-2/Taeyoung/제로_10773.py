import sys

input = sys.stdin.readline

K = int(input().strip())

stack = []

for _ in range(K):
    n = int(input().strip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
