n = int(input())
t, r = n, 0
while t:
    if t%5 == 0: t, r = t//5, r+1
    else: n = t = n-1
print(r)
# 32412 kb
# 40ms

n = int(input())
d, r = 5, 0
while n//d: d, r = d*5, r+n//d
print(r)
# 32412 kb
# 36ms