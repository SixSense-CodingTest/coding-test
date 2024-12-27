import sys

input = sys.stdin.readline

T = int(input())
numbers= [0] * 11
numbers[1] = 1
numbers[2] = 2
numbers[3] = 4

for _ in range(T):
    n = int(input())
    for i in range(4, n+1):
        numbers[i] = numbers[i-1] + numbers[i-2] + numbers[i-3]
    print(numbers[n])

    

