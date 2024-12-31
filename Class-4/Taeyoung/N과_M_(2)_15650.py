import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

for i in list(combinations(list(range(1, N+1)), M)):
    print(*i)

'''
메모리 : 32412 KB
시간 : 36 ms
'''