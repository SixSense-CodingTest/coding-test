# N개의 행, M개의 열의 체스판
# 8x8 체스판으로 만듦
# 첫번째 값이 검은색이냐 흰색이냐로 나누어서 계산
# 이중 다시 칠해야 하는 정사각형 개수 최솟값 출력
# 변 공유하는 두개의 사각형 => 다른 색
# 
import sys


input= sys.stdin.readline
N, M = map(int, input().split())
boards = [input().strip() for _ in range(N)]



def check_boards(y, x, start, boards):
    count = 0
    for i in range(8):
        for j in range(8):
            if start == 'B':
                board = 'B' if (i+j) % 2 == 0 else 'W'
            elif start =='W':
                board = 'W' if (i+j) % 2 ==0 else 'B'
            
            if boards[y+i][x+j] != board:
                count += 1
    return count
                

answer = N * M
for i in range(N-7):
    for j in range(M-7):
        start_W = check_boards(i, j, 'W', boards)
        start_B = check_boards(i, j, 'B', boards)
        answer = min(answer, start_W, start_B)

print(answer)