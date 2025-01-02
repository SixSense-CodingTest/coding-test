N = int(input())

L1 = list(map(int,input().split()))
L2 = sorted(L1)

res = {}

cnt = 0
for i in range(len(L2)):
    if L2[i] in res.keys():
        pass
    else:
        res[L2[i]] = cnt
        cnt+=1 

print(*[res[i] for i in L1])