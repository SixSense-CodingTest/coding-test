from collections import deque
n, k = map(int, input().split())
v = [1] * 100001
vd = [1] * 100001
q = deque([(n, 0)])
while q:
    t, c = q.popleft()
    while t < 100001 and vd[t]:
        if t == k: break
        v[t] = 0
        vd[t] = 0
        for i in [t+1, t-1]:
            if -1 < i < 100001 and v[i]:
                v[i] = 0
                q.append((i, c+1))
        t *= 2
    else: continue
    break
print(c)
# 36024kb
# 132ms

from collections import deque
n, k = map(int, input().split())
v = [2] * 100001
q = deque([(n, 0)])
while q:
    t, c = q.popleft()
    while t < 100001 and v[t]:
        if t == k: break
        v[t] = 0
        for i in [t+1, t-1]:
            if -1 < i < 100001 and v[i] > 1:
                v[i] = 1
                q.append((i, c+1))
        t *= 2
    else: continue
    break
print(c)
# 35300kb
# 128ms