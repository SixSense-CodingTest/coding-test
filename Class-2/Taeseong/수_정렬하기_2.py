N = int(input())

L = [0]*1000001*2
for _ in range(N):
    tmp = int(input())
    L[tmp+1000000] = 1 

for idx,val in enumerate(L):
    if val == 1:
        print(idx-1000000)
