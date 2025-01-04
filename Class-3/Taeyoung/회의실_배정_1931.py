import sys

input = sys.stdin.readline

N = int(input().strip())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[0]))

max_end = cnt = 0

for start, end in arr:
    if max_end <= start:
        max_end = end
        cnt += 1

print(cnt)

'''
메모리 : 60360 KB
시간 : 248 ms
'''