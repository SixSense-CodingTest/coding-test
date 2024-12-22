import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())

no_see = set()
no_hear = set()
for _ in range(N):
    name = input().strip()
    no_see.add(name)

for _ in range(M):
    name = input().strip()
    no_hear.add(name)

ans = []
for name in no_see:
    if name in no_hear:
        ans.append(name)
ans.sort()
print(len(ans), *ans, sep= '\n')

"""
PyPy3
메모리 : 120736 KB
시간 : 148 ms
"""