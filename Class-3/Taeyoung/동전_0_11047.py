import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    A = int(input().strip())
    if A <= K:
        coins.append(A)

cnt = 0

for i in reversed(coins):
    if K == 0:
        break
    cnt += K // i
    K = K % i
print(cnt)

'''
메모리 : 32412 KB
시간 : 44 ms
'''
