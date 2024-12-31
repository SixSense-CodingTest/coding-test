import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

for i in list(permutations(num_list, M)):
    print(*i)

'''
메모리 : 37528 KB
시간 : 144 ms
'''