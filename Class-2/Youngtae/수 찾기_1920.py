import sys

input = sys.stdin.readline
N = int(input())
A = set(list(map(int, input().split())))

M = int(input())
B = list(map(int, input().split()))


for i in range(len(B)):
    if B[i] in A:
        print(1)
    else:
        print(0)