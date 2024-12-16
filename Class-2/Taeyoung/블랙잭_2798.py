# 브루트포스
import sys

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

max_hap = N

for i in cards:

    for j in cards:
        if i == j: continue

        for k in cards:
            if i == k or j == k: continue

            hap = i + j + k

            if hap <= M and max_hap < hap : 
                max_hap = hap

print(max_hap)

# 조합으로 풀기
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
combi = list(combinations(cards, 3))

under_M = [sum(i) for i in combi if sum(i)<=M]
print(max(under_M))