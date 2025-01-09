from itertools import permutations

N,M = list(map(int,input().split()))
case = list(map(int,input().split()))

for i in sorted(list(set(permutations(case,M)))):
    print(*i)
