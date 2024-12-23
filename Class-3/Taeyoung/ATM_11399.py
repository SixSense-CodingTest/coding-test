import sys

input = sys.stdin.readline
N = int(input())

people = list(map(int, input().split()))
people.sort()

result = 0

for i in range(1, len(people)+1):
    result += sum(people[:i])

print(result)

'''
메모리 : 32412 KB
시간 : 44 ms
'''