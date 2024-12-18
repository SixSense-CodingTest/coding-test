# 좌표를 x좌표 증가 , 같으면 y좌표 증가하는 순서로 정렬
import sys

N = int(sys.stdin.readline())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x,y])

points.sort(key=lambda x : [x[0],x[1]])

for x, y in points:
    print(x, y)
