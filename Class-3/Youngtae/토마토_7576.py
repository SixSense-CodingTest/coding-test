# 상하좌우로 익음 => 1이 토마토
# -1은 토마토 안들어있음
# 다 익지못하면 -1 출력, 처음부터 다익어있으면 0 출력
# 토마토 모두 익을때까지 최소 날짜 출력


## 1번 풀이
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            queue.append((i,j))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<= ny < N and 0 <= nx < M and boxes[ny][nx] == 0:
            boxes[ny][nx] = boxes[y][x] + 1
            queue.append((ny,nx))

max_days = 0
for row in boxes:
    for value in row:
        if value == 0:
            print(-1)
            sys.exit()
        max_days = max(max_days, value)

print(max_days - 1)


## 2번 풀이
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
unripe_count = 0
max_days = 0

for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            queue.append((i,j))
        elif boxes[i][j] == 0:
            unripe_count += 1

if unripe_count == 0:
    print(0)
    sys.exit()
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0<= ny < N and 0 <= nx < M and boxes[ny][nx] == 0:
            boxes[ny][nx] = boxes[y][x] + 1
            queue.append((ny,nx))
            unripe_count -= 1
            max_days = boxes[ny][nx]

if unripe_count > 0:
    print(-1)
else:
    print(max_days - 1)

