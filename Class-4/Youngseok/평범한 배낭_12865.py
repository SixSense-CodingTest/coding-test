import sys
input = sys.stdin.readline
n, capacity = map(int, input().split())
dp = {0:0}
for _ in range(n):
    w, v = map(int, input().split())
    tmp = {}
    for weight, value in dp.items():
        nw, nv = weight+w, value+v
        if nw <= capacity:
            if dp.get(nw, 0) < nv: tmp[nw] = nv
    dp.update(tmp)
print(max(dp.values()))
# 42976kb
# 984ms

import sys
input = sys.stdin.readline
n, capacity = map(int, input().split())
dp = {0:0}
for _ in range(n):
    w, v = map(int, input().split())
    tmp = {}
    for weight, value in dp.items():
        nw, nv = weight+w, value+v
        if nw > capacity: continue
        if dp.get(nw, 0) < nv: tmp[nw] = nv
    dp.update(tmp)
print(max(dp.values()))
# 42976kb
# 916ms

import sys
input = sys.stdin.readline
n, capacity = map(int, input().split())
dp = {0:0}
for _ in range(n):
    w, v = map(int, input().split())
    tmp = {}
    for value, weight in dp.items():
        nw, nv = weight+w, value+v
        if dp.get(nv, capacity+1) > nw: tmp[nv] = nw
    dp.update(tmp)
print(max(dp))
# 36320kb
# 612ms

import sys
input = sys.stdin.readline
n, capacity = map(int, input().split())
dp = {0:0}
wvlist = [tuple(map(int, input().split())) for _ in range(n)]
wvlist.sort(reverse=True)
for w, v in wvlist:
    tmp = {}
    for value, weight in dp.items():
        nw, nv = weight+w, value+v
        if dp.get(nv, capacity+1) > nw: tmp[nv] = nw
    dp.update(tmp)
print(max(dp))
# 36320kb
# 464ms
# sort하면 w가 큰 것 부터 들어가서 capacity 보다 큰 값이 앞 부분에서 많이 걸러져서 속도 빨라지는 듯