n = int(input())
t = sorted(map(int, input().split()))
r = 0
for i in t: r, n = r+n*i, n-1
print(r)
# 32412kb
# 40ms