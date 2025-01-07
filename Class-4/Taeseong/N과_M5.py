from itertools import permutations

N,M = list(map(int,input().split()))

K = list(map(int,input().split()))

for i in sorted(list(permutations(K,M))):
    print(*i)