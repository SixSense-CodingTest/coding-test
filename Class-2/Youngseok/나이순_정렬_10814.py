import sys
input = sys.stdin.readline
n = int(input())
user = sorted([input() for i in range(n)], key = lambda x : int(x.split()[0]))
print(''.join(user))