import sys
from math import factorial

input = sys.stdin.readline

N = int(input().rstrip())

cnt = 0
for i in reversed(str(factorial(N))):
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break

'''
메모리 : 34536 KB
시간 : 44 ms
'''