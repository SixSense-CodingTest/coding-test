# 각 집 RGB 중 하나로 색칠
# 모든 집을 칠하는 비용의 최솟값
# 1번 집의 색 != 2번 집의 색
# N번 집의 색은 N-1 집의 색과 같지 않아야 함
# i(2<= i <= N-1)번 집의 색은 i-1번, i+1번 집의 색과 달라야함
# 그냥 앞에 집의 색깔이랑 다르면됨 1번부터 N까지
# 앞전에 어떤 색깔 골랐는지 확인하고 다른 것 중에 최솟값 고르기

import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]

prev = cost[0]


for i in range(1,N):
    current = [0] * 3
    current[0] = cost[i][0] + min(prev[1], prev[2])
    current[1] = cost[i][1] + min(prev[0], prev[2])
    current[2] = cost[i][2] + min(prev[0], prev[1])
    prev = current

print(min(prev))
