t = set([2])
for i in range(3, 1000):
    for j in t:
        if i % j == 0: break
    else: t.add(i)
n, l = input(), map(int, input().split())
res = 0
for i in l:
    if i in t: res += 1
print(res)