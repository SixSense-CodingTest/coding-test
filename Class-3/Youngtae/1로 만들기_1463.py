# 3으로 나누기
# 2로 나누기
# 1을 빼기
# 정수 N이 주어졌을 때, 연산 세개 이용해서 1만들기 => 연산 횟수의 최솟값 출력
# 모든 경우를 다 해보고 연산 최솟값을 출력하게 하기

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])

    
# 메모리 40224 kb , 시간 456ms