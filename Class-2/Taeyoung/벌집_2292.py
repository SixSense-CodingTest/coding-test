import sys

N = int(sys.stdin.readline().strip())

cnt = total = 1
while N > total:
    total += 6*cnt
    cnt += 1

print(cnt)

'''
메모리 : 32412 KB
시간 : 40 ms
'''
