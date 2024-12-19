N = int(input())
Ns = list(map(int,input().split()))
M = int(input())
Ms = list(map(int,input().split()))

res = {i:0 for i in Ms}
for n in Ns:
    if n in res.keys():
        res[n]+=1

for m in Ms:
    print(res[m],end=' ')
