N,K = list(map(int,input().split()))

L = list(range(1,N+1))
point = (K-1)%N

res = []
while True:
    res.append(str(L[point]))
    L.remove(L[point])
    if not L:
        break
    point = (point+K-1)%len(L)

print('<',', '.join(res),'>',sep='')