# 각 회의가 겹치지 않게 하면서 회의실 사용가능한 회의 최대 개수
# 회의 시작 시간, 끝나는 시간 주어짐
# 우선 정렬을 하고 작은것부터 시작을 하는데, 그때그때 조건에 맞는 회의 선택

import sys
input = sys.stdin.readline

N = int(input())
room = []

for _ in range(N):
    start, end = map(int, input().split())
    room.append((start,end))

room.sort(key = lambda x: (x[1],x[0]))

count = 0
last_end = 0
for start, end in room:
    if start >= last_end:
        count += 1
        last_end = end
        
print(count)



