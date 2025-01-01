# 한 변의 길이 N
# 상자안에 색깔이 통일될때까지 4등분을 반복 => 길이 1 될때까지 반복
# 0으로만 이루어진 상자 count, 1로만 이루어진 상자 count
# 재귀 느낌? 자른 상자안에서 또 함수 호출해서 상자 찾기
# N이 1이되거나 상자안 색상 통일되면 종료
# 이때 그 색상이 0이면 하얀색 count + 1, 1이면 파란색 count + 1

import sys
input = sys.stdin.readline

white_count = 0
blue_count = 0

def is_uniform_color(board, x, y, size):
    color = board[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if board[i][j] != color:
                return False
    return True

def count_color(board, x, y, size):
    global white_count, blue_count

    if is_uniform_color(board, x, y, size):
        if board[y][x] == 0:
            white_count += 1
        else:
            blue_count += 1
        return

    half = size // 2
    count_color(board, x, y, half)           # 왼쪽 위
    count_color(board, x + half, y, half)   # 오른쪽 위
    count_color(board, x, y + half, half)   # 왼쪽 아래
    count_color(board, x + half, y + half, half)  # 오른쪽 아래

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

count_color(board, 0, 0, N)

print(white_count)
print(blue_count)