from itertools import permutations
n, m = map(int, input().split())
for i in permutations(sorted(input().split(), key = int), m): 
    print(' '.join(i)+'\n')
# 32412kb
# 64ms