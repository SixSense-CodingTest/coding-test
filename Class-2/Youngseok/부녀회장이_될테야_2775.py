import sys
from math import comb
input=sys.stdin.readline
t = int(input())
for i in range(t):
    n, m = int(input()), int(input())
    print(comb(n+m, m-1))