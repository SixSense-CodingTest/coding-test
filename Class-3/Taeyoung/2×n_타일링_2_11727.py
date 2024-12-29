import sys

input = sys.stdin.readline

n = int(input().strip())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    prev2, prev1 = 1, 3

    for i in range(3, n+1):
        curr = (prev2*2 + prev1) % 10007
        prev2, prev1 = prev1, curr

    print(prev1)

'''
메모리 : 32544 KB
시간 : 40 ms
'''
