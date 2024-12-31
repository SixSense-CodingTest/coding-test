import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    half = (start+end)//2

    result = sum(i-half for i in trees if i-half >= 0)
    if result < M:
        end = half-1
    else:
        start = half+1

print(end)

'''
메모리 : 148224 KB
시간 : 2740 ms
'''