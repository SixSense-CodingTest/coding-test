import sys
input = sys.stdin.readline

N,M = list(map(int,input().strip().split()))

L = list(map(int,input().strip().split()))

# L.sort()

LL = [0]

for i in range(len(L)):
    LL.append(LL[i]+L[i])


for _ in range(M):
    
    i, j = list(map(int,input().strip().split()))

    print(LL[j] - LL[i-1])
