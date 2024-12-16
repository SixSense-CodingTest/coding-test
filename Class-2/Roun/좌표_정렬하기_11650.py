############
# silver 5 #
############

import sys

input = sys.stdin.readline

num = int(input())
points = []

for i in range(num):
    x, y = map(int, input().split())

    points.append([x, y])

points.sort(key=lambda x: (x[0], x[1]))

for x, y in points:
    print(f"{x} {y}")

###################
# memory: 55240KB #
# time:   325ms   #
###################

# 기모아서 출력하려다가 시간 초과남