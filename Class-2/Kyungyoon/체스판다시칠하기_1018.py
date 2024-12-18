N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def check_count(sliding_board, correct):
    # 8x8 보드와 타겟 체스판의 차이를 카운트하는 함수
    count = 0
    for i in range(8):
        for j in range(8):
            if sliding_board[i][j] != correct[i][j]:
                count += 1
    return count

# 8 by 8로 나눠야하는지 모르고 짠 코드
# correct1 = ['W', 'B'] * (int(M/2) + 1)
# correct2 = ['B', 'W'] * (int(M/2) + 1)

# 정답
correct1 = [
    ['W', 'B'] * 4,
    ['B', 'W'] * 4,
] * 4

correct2 = [
    ['B', 'W'] * 4,
    ['W', 'B'] * 4,
] * 4

ans = float('inf')
for i in range(N - 7): # 8 by 8이니까
    for j in range(M - 7):
        # sliding board 만들기
        sliding_board = [row[j:j+8] for row in board[i:i+8]]

        # 두 가지 경우
        ans1 = check_count(sliding_board, correct1)
        ans2 = check_count(sliding_board, correct2)

        ans = min(ans, ans1, ans2)
print(ans)

"""
PyPy3
메모리 : 111496 KB
시간 : 116 ms
"""