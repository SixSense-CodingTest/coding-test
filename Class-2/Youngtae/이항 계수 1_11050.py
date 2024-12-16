N ,K = map(int, input().split())

bunmo = 1
bunza = 1

for i in range(1, K + 1):
    bunmo *= i

for i in range(N-K+1, N+1):
    bunza *= i

print(bunza // bunmo)
