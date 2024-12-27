import sys
print = sys.stdout.write
m, n = map(int, input().split())
t = []
for i in range(2, m):
    for j in t: 
        if i**(1/2) < j:
            t.append(i)
            break
        elif i % j == 0: break
    else: t.append(i)

for i in range(max(2,m), n+1):
    for j in t: 
        if i**(1/2) < j:
            t.append(i)
            print(f'{i}\n')
            break
        elif i % j == 0: break
    else: 
        t.append(i)
        print(f'{i}\n')
# 36100kb
# 3648ms

m, n = map(int, input().split())
t = [False, False]+[True]*(n-1)
for i in range(2, int(n**(1/2))+1):
    if t[i]:
        for j in range(i*i, n+1, i):
            t[j] = False

for i in range(m, n+1):
    if t[i]: print(i)
# 47760kb
# 292ms

m, n = map(int, input().split())
t = [False, False]+[True]*(n-1)
for i in range(2, int(n**(1/2))+1):
    if t[i]:
        for j in range(i*i, n+1, i):
            t[j] = False
print('\n'.join([f'{i}' for i in range(m, n+1) if t[i]]))
# 47760kb
# 256ms
