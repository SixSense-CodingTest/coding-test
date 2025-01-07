from itertools import combinations

N,M = list(map(int,input().split()))
for i in combinations(list(range(1,N+1)),M):
    print(*i)