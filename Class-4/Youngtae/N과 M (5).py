# N, M
# N개의 자연수와 M이 주어졌을때, 길이 M인 수열 모두 구하기

import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for permutation in permutations(numbers, M):
    print(" ".join(map(str, permutation)))

