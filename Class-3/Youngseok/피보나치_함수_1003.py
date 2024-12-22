import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, a, b = int(input()), 1, 0
    for j in range(n): a, b = b, a+b
    print(a, b)
# 32412kb
# 32ms