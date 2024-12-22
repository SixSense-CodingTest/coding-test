import sys
input = sys.stdin.readline
n, m = map(int,input().split())
nl = set(input() for _ in range(n))
res = [i for _ in range(m) if (i := input()) in nl]
print(len(res))
print(''.join(sorted(res)))
# 37532kb
# 64ms