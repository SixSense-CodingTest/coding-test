N, K = map(int, input().split())

dp = [0] * (K + 1) # dp[i] : 용량이 i일 때 얻을 수 있는 최대가치

for _ in range(N):
    W, V = map(int, input().split())
    # 앞의 값이 업데이트돼서 뒤의 값에 영향주지않게 역방향 탐색
    for j in range(K, W - 1, -1):
        dp[j] = max(dp[j], dp[j - W] + V) 
        # max(
        # 물건을 선택하지 않은 경우 최대가치 = 용량이 j일때 얻을 수 잇는 최대가치
        # 물건을 선택하는 경우 최대가치 = 남은 용량에서 얻을 수 있는 최대 가치 + 현재 물건의 가치
        # )

print(dp[K])

"""
PyPy3
메모리 : 110328 KB
시간 : 136 ms
"""