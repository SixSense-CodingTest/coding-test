import sys
input = sys.stdin.readline
v = [0, 0, 0]
for _ in range(int(input())):
    r, g, b = map(int, input().split())
    v[0], v[1], v[2] = min(v[1], v[2]) + r, min(v[0], v[2]) + g, min(v[0], v[1]) + b
print(min(v))
# 32412kb
# 40ms