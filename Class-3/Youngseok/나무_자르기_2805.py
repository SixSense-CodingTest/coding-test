n, m = map(int, input().split())
l = list(map(int, input().split()))
mx = max(l)
mn = max(mx-m, 0)
while mn <= mx:
    mid = (mn + mx) // 2
    if sum(max(i - mid, 0) for i in l) < m: mx = mid - 1
    else: mn = mid + 1
print(mx)
# 145580kb
# 2732ms

n, m = map(int, input().split())
l = sorted(map(int, input().split()), reverse=True)
mx = l[0]
mn = max(mx-m, 0)
while mn <= mx:
    mid = (mn + mx) // 2
    s = 0
    for i in l:
        if (t:=i-mid) > 0 : s += t
        else: break
    if s < m: mx = mid - 1
    else: mn = mid + 1
print(mx)
# 시간초과

n, m = map(int, input().split())
d = {}
for x in map(int, input().split()):
    if x in d: d[x]+=1
    else: d[x]=1
mx = max(d)
mn = max(mx-m, 0)
while mn <= mx:
    mid = (mn + mx) // 2
    if sum(max(0, (i-mid)*d[i]) for i in d) < m: mx = mid - 1
    else: mn = mid + 1
print(mx)
# 120004kb
# 496ms