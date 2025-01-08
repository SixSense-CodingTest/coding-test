# 수열 A의 가장 긴 증가하는 부분 수열 길이 출력하기
# set으로 중복만 없애고 정렬

import sys
input = sys.stdin.readline

A = int(input())
numbers = list(map(int, input().split()))

dp = [1] * A
for i in range(A):
    for j in range(0, i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))