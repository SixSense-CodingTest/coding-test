# N, M 입력받고 N X N 크기 표 입력으로 받고 M 횟수만큼 x1 y1 x2 y2 입력 넣어주기
# x,y 는 x행 y열 의미
# 2,2 부터 3,4 까지면 2,3 2,4 3,2 3,3 3,4 를 합해야함

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# boards = [list(map(int, input().split())) for _ in range(N)]

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     sum_num = 0
#     for i in range(x1-1, x2):
#         for j in range(y1-1,y2):
#             sum_num += boards[i][j]
#     print(sum_num)

# 시간 초과 O(N^2*M) 인 느낌?

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(N)]

# 누적 합 테이블 생성
S = [[0] * (N + 1) for _ in range(N + 1)]  
for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = boards[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(total)
    