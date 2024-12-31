import sys
from math import gcd

input = sys.stdin.readline

T = int(input().strip())

def year_count(m, n, x, y):
    k = x

    while k <= m*n // gcd(m, n):
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
    return -1

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(year_count(M, N, x, y))

'''
메모리 : 34536 KB
시간 : 2856 ms
'''