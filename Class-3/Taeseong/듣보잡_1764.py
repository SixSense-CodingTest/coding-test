import sys

input = sys.stdin.readline

N, M = list(map(int,input().strip().split()))

not_heard = set()
not_saw = set()

for _ in range(N):
    not_heard.add(input().strip())

for _ in range(M):
    not_saw.add(input().strip())

res = sorted(not_heard.intersection(not_saw))
print(len(res))
print(*res,sep='\n')