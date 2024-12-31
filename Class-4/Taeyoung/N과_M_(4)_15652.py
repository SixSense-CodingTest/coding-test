import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())

# 1부터 N까지의 중복 조합 생성
for combination in combinations_with_replacement(range(1, N + 1), M):
    print(*combination)

'''
메모리 : 33432 KB
시간 : 52 ms
'''
