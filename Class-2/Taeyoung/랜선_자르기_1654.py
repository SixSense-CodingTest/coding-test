import sys

input = sys.stdin.readline

K, N = map(int, input().split())

LANs = [int(input().rstrip()) for _ in range(K)]

start = 1
end = max(LANs)

while start <= end:
    half = (start + end) // 2
    result = 0
    for i in LANs:
        result += i // half

    if result >= N:
        start = half + 1
    else:
        end = half - 1

print(end)

'''
메모리 : 33432 KB
시간 : 84 ms
'''
