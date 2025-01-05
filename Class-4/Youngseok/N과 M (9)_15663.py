from itertools import permutations
n, m = map(int, input().split())
v = set()
for i in permutations(sorted(input().split(), key = int), m): 
    if (st:=' '.join(i)) in v: continue
    print(st)
    v.add(st)
# 37024kb
# 56ms