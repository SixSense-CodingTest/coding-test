from collections import deque
n, k = map(int, input().split())
v = [1] * 100001
q = deque([(n, 0)])
while q:
    t, c = q.popleft()
    if t == k: break
    for i in [t*2, t+1, t-1]:
        if -1 < i < 100001 and v[i]:
            v[i] = 0
            q.append((i, c+1))
print(c)
# 36264kb
# 124ms