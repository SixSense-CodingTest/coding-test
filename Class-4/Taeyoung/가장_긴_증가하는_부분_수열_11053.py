import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))

'''
메모리 : 32412 KB
시간 : 128 ms
'''