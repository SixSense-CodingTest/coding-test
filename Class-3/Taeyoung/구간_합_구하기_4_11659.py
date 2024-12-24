import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sum = 0
prefix_sum = []
for i in list(map(int, input().split())):
    sum += i
    prefix_sum.append(sum)


for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(prefix_sum[b-1])
    else:
        print(prefix_sum[b-1] - prefix_sum[a-2])

'''
메모리 : 41144 KB
시간 : 228 ms
'''
