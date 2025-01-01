# 1 => 배추가 심어져있는 땅
# 0 => 배추 없는 땅
# 흰 지렁이 있는 곳에 배추 인접해 있으면 해충 보호됨 -> 상하좌우
# 최소 필요한 지렁이 개수 출력
# 우선 M x N 배열 생성
# X, Y 로 배추 위치 1로 저장
# DFS로 푸는 느낌 1이 나올때까지 계속 탐색하다가 더이상 방문안한 1이 없을때 count + 1 하면 될 느낌


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

directions = [[-1,0], [1,0], [0,1] , [0,-1]]

def dfs(x,y):
    visited[y][x] = True

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and ground[ny][nx] == 1:
            dfs(nx,ny)


T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().strip().split()) # M 가로길이 N 세로길이 K 배추 개수
    ground = [[0] * M for _ in range(N)] # 배추밭 생성
    visited = [[False] * M for _ in range(N)]
    worm_count = 0
    
    for _ in range(K):
        X, Y = map(int, input().strip().split())  # 배추의 위치
        ground[Y][X] = 1

    for y in range(N):
        for x in range(M):
            if ground[y][x] == 1 and not visited[y][x]:
                dfs(x,y)
                worm_count += 1
    print(worm_count)
