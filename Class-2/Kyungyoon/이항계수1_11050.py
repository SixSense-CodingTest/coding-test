from itertools import combinations
N, K = map(int, input().split())
print(len(list(combinations(list(range(N)), K))))


"""
PyPy3
메모리 : 108384KB
시간 : 92ms

Python3
메모리 : 32412KB
시간 : 40ms
"""