# 수 N개 주어졌을 때 i번째 수부터 j번째 수 합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sum_num = [0] * (N+1)
for i in range(1,N+1):
    sum_num[i] = sum_num[i-1] + numbers[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_num[j]-sum_num[i-1])