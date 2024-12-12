############
# bronze 2 #
############

import sys

input = sys.stdin.readline

_ = int(input())
numbers = list(map(int, input().rstrip().split()))

# 0은 아직 확인하지 않음
# 1은 소수
# 2는 누군가의 배수
dp = [0] * (max(numbers) + 1)

for i in range(2, max(numbers) + 1):
    if dp[i] == 0:
        dp[i] = 1
    
        for j in range(i + i, max(numbers)+1, i):
            dp[j] = 2

count = 0

for number in numbers:
    if dp[number] == 1:
        count += 1

print(count)

###################
# memory: 32412KB #
# time:   36ms    #
###################

# 최적화 방안

# 1. for i in range(2, int(max(numbers) ** 0.5) + 1)
# 에라토스테네스의 체 (소수의 배수 체크를 반복적으로 수행 -> 최적화)
# 이 범위 내에서 쭉 소수가 아닌 것을 체크하고 나머지 처리하기

# 2. for j in range(i*i, max(numbers) + 1, i) 로 변경 가능
# 배수 계산 범위를 i*i 이상으로 시작하면 이미 방문한 배수를 중복 체크하지 않아도 됨