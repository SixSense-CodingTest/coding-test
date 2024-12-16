import sys
input = sys.stdin.readline
n = int(input())
p = sorted([input() for _ in range(n)])
p.sort(key = lambda x: tuple(map(int, x.split())))
print(''.join(p))