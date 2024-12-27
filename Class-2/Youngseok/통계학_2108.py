import sys
from collections import Counter as C
ip = sys.stdin.readline
l = sorted([int(ip()) for _ in range(int(ip()))])
f = C(l)
print(int(m+0.5) if (m:=sum(l)/len(l))>0 else int(m-0.5))
print(l[len(l)//2])
print(i[1] if len(i:=[k for k, v in f.items() if v == max(f.values())]) > 1 else i[0])
print(max(l)-min(l))
# 53796kb
# 1576ms

import sys
from collections import Counter as C
ip = sys.stdin.readline
l = sorted([int(ip()) for _ in range(int(ip()))])
f = C(l).most_common(2)
print(int(m+0.5) if (m:=sum(l)/len(l))>0 else int(m-0.5))
print(l[len(l)//2])
print(f[1][0] if len(f)>1 and f[0][1] == f[1][1] else f[0][0])
print(l[-1]-l[0])
# 59588kb
# 344ms

import sys
from collections import Counter as C
ip = input
f = C(int(ip()) for i in range(int(ip())))
l = sorted(list(f.elements()))
print(int(m+0.5) if (m:=sum(l)/len(l))>0 else int(m-0.5))
print(l[len(l)//2])
print(f[1][0] if len((f:=sorted(f.items(), key=lambda x: (-x[1], x[0]))))>1 and f[0][1] == f[1][1] else f[0][0])
print(l[-1]-l[0])
# 44076kb
# 224ms

import sys
ip = sys.stdin.readline
n = int(ip())
l, c, d, s = [], [], {}, 0
mn, mx, ct = 4000, -4000, 0
for _ in range(n):
    v = int(ip())
    s+=v
    l.append(v)
    if v < mn: mn = v
    if v > mx: mx = v
    if v not in d: d[v] = 0
    d[v] += 1
    if ct < d[v]: ct, c = d[v], [v]
    elif ct == d[v]: c.append(v)
l.sort(), c.sort()
print(int(s/n+0.5) if s>0 else int(s/n-0.5))
print(l[n//2])
print(c[1] if len(c)>1 else c[0])
print(mx-mn)
# 53796kb
# 576ms
