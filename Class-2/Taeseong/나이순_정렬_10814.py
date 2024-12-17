N = int(input())

P = [] 
for _ in range(N):
    age,name = list(input().split())
    P.append((int(age),name))


P.sort(key=lambda x:x[0])


[print(*p[:2]) for p in P]
