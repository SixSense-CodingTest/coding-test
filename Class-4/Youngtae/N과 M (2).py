# 1부터 N까지 자연수 중에서 중복 없이 M개 고른 수열
# 고른 수열 오름차순
# 수열을 모두 구하기

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [i for i in range(1,N+1)]

for combination in combinations(numbers, M):
    print(" ".join(map(str, combination)))

