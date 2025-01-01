import sys

input = sys.stdin.readline

N = int(input().strip())

num_dict = {}

for _ in range(N):
    num = int(input().strip())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

for key, value in sorted(num_dict.items()):
    for _ in range(value):
        print(key)

'''
메모리 : 34456 KB
시간 : 10168 ms
'''