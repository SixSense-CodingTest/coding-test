"""
백트래킹 : 조건을 만족하는 경로만 탐색하기 위해 가지치기를 포함하는 탐색기법(해를 찾는 과정에서 가능성이 없는 경로를 제거)
    - 해를 구하기 위한 탐색
    - N과 M의 문제, 순열조합문제 등
DFS : 모든 경로를 탐색하는 단순 탐색 기법
    - 그래프의 모든 노드를 탐색할 때
"""
N = int(input())
cnt = 0
queen_pos = [-1]*N  # 각 행의 퀸 열 위치 저장

row = 0  # 현재 퀸을 배치하려는 행(0번째 행부터 탐색 시작)

while row >= 0:
    flag = False # 현 행에 퀸을 배치했는지 여부

    # 현재 행에서 탐색을 시작할 열
    if queen_pos[row] == -1:
        start_col = 0
    else:
        start_col = queen_pos[row] + 1 # 이전에 퀸을 놓았던 위치 다음 열부터 시작

    # 현재 행에서 가능한 열 탐색
    for col in range(start_col, N):
        # 이전 행들과 충돌 여부 확인 : 같은 열에 있는지, 대각선에 있는지
        for r in range(row):
            if queen_pos[r] == col or abs(queen_pos[r] - col) == abs(r - row):
                break
        else:
            # 유효한 열을 찾으면 퀸 배치
            queen_pos[row] = col
            flag = True # 배치했으니 flag 바꿔주기
            break
    
    # 퀸을 배치한 경우
    if flag:
        if row == N - 1:  # 마지막 행까지 퀸 배치 완료
            cnt += 1 # 해 1개 찾음
            queen_pos[row] = -1  # 마지막 행 초기화 후 (이전 행으로 돌아가 다른 경우의 수 탐색)
        else:
            row += 1  # 다음 행으로 이동
            continue
    # 퀸을 배치하지 못 한 경우 : 이전 행으로 (돌아가 다른 경로 탐색할 준비)
    else:
        queen_pos[row] = -1  # 현재 행 초기화

    row -= 1  # 이전 행으로 돌아가는 부분

print(cnt)

"""
PyPy3
메모리 : 112124 KB
시간 : 29688 ms
"""