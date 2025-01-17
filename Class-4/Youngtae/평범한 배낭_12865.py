# 각 물건 무게 W, 가치 v
# 최대 무게 K 일때 가치의 최댓값?
# 작은 무게부터 최대가치를 계산하고 dp에 현재 합산 무게와 가치의 최댓값만을 저장한다.
# 최종 출력은 dp[N]이 될듯 


import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W,V))

dp = [0] * (K+1)

for W, V in items:
    for k in range(K, W-1, -1):
        dp[k] = max(dp[k], dp[k-W] + V)

print(dp[K])


