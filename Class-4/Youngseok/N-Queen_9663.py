n = int(input())
res = [0]
row = [0] * n
def lay_queen(num_queen):
    if num_queen == n: res[0] += 1
    else:
        for i in range(n):
            for j in range(num_queen):
                if i == row[j] or abs(i-row[j]) == abs(num_queen-j): break
            else:
                row[num_queen] = i
                lay_queen(num_queen+1)
lay_queen(0)
print(res[0])
# python3 는 시간초과
# pypy3 은 16560ms

n = int(input())
def n_queen(row, cols, diags1, diags2):
    if row == n: return 1
    count = 0
    available = ((1 << n) - 1) & ~(cols | diags1 | diags2)
    while available:
        pos = available & -available
        available -= pos
        count += n_queen(
            row + 1,
            cols | pos,
            (diags1 | pos) << 1,
            (diags2 | pos) >> 1
        )
    return count
print(n_queen(0, 0, 0, 0))
# gpt 피셜 최적화
# 보드에 대한 정보를 변수 4개에 다 때려박음
# (1 << n) - 1 << 한 줄에 퀸을 놓을 수 있는지 여부를 n 개 비트로 표현
# ~(cols | diags1 | diags2) 같은 라인에 퀸이 존재하는지, 대각선에 존재하는지 확인해서 제외
# 만약 이 값이 0이면 해당 라인에 놓을 수 있는 퀸 없음
