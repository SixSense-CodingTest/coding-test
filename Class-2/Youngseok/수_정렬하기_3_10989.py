import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
v = [0] * 10001
for i in range(n): v[int(input())] += 1
for i in range(1,10001):
    for j in range(v[i]): print(f'{i}\n')