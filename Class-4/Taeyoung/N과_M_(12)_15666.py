import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

# 1부터 N까지의 중복 조합 생성
for combination in sorted(set(combinations_with_replacement(num_list, M)), key= lambda x: ([x[i] for i in range(M)])):
    print(*combination)

'''
메모리 : 33432 KB
시간 : 42 ms
'''
