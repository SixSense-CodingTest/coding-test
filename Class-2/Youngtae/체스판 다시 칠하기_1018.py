# N개의 행, M개의 열의 체스판
# 8x8 체스판으로 만듦
# 첫번째 값이 검은색이냐 흰색이냐로 나누어서 계산
# 이중 다시 칠해야 하는 정사각형 개수 최솟값 출력
# 변 공유하는 두개의 사각형 => 다른 색
# 열 : 0 < index < M
# 행: 0 < index < N 

import sys


input= sys.stdin.readline
N, M = map(int, input())
boards = []


for _ in range(N):
    hang = list(input())
    boards.append(hang)


# for i in range(N-8):
#     for j in range(M-):
#         if board[i]


        







