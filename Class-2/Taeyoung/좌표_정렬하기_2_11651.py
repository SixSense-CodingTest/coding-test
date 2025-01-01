import sys

input = sys.stdin.readline

N = int(input().strip())

num_list = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

for i, j in num_list:
    print(i, j)

'''
메모리 : 61144 KB
시간 : 332 ms
'''