n = int(input())
l = list(map(int, input().split()))
d = {}
c = 0
for i in sorted(l):
    if i in d: continue
    d[i] = f'{c}'
    c += 1
print(' '.join(map(lambda x: d[x], l)))
# 145580kb
# 1568ms