import sys
ip = sys.stdin.readline
if n:=int(ip()):
    l = sorted([int(ip()) for _ in range(n)])
    if r:=int(0.5+n*0.15): l = l[r:-r]
    print(int(0.5+sum(l)/(len(l))))
else: print(0)
# 39000kb
# 136ms

import sys
ip = sys.stdin.readline
if n:=int(ip()):
    l = [int(ip()) for _ in range(n)]
    l.sort()
    if r:=int(0.5+n*0.15): l = l[r:-r]
    print(int(0.5+sum(l)/(len(l))))
else: print(0)
# 37164kb
# 152ms
## .sort() 가 sorted() 보다 좀 더 느린데 메모리를 덜 쓰는듯

import sys
ip = sys.stdin.readline
n=int(ip())
l = sorted([int(ip()) for _ in range(n)])
if r:=int(0.5+n*0.15): l = l[r:-r]
print(int(0.5+sum(l)/(len(l) or 1)))
# 39000kb
# 140ms
## 제로 디비전 특이하게 해결하는 법 찾아서 써봄