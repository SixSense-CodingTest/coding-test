N = int(input())
T = list(map(int,input().split()))
T.sort()

res = [T[0]]
tmp = T[0]
for t in range(1,len(T)):
    res.append(T[t]+tmp)
    tmp+=T[t]

print(sum(res))