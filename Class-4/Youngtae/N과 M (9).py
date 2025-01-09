import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

permutation_list = permutations(numbers, M)
final_permutations = sorted(set(permutation_list))

for permutation in final_permutations:
    print(" ".join(map(str, permutation)))
