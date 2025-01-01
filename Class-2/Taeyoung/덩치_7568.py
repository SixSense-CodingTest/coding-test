import sys

input = sys.stdin.readline

N = int(input().rstrip())

people = [list(map(int, input().split())) for _ in range(N)]

rank = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank[i] += 1

print(" ".join(map(str, rank)))

'''
메모리 : 32412 KB
시간 : 36 ms
'''