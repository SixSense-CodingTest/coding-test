import sys
input = sys.stdin.readline
n = int(input())
v = [input() for _ in range(n)]
v.sort(key = lambda x: int(x))
print(''.join(v))