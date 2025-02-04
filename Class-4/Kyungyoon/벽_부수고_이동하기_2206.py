"""
문제조건
- 0은 이동가능, 1은 벽
- (1,1)에서 (N,M)까지 이동하려는데, 최단경로
- 시작하는 칸, 끝나는 칸 포함해서 센다
- 1개의 벽 부수면 경로가 짧아지면, 1개까지는 부셔도 된다

해결방법
- 벽을 부쉈는지 여부를 고려해야해서, 3차원 리스트 사용 : visited[y][x][벽 부쉈는지 여부]
- 다음 위치가 0이면 이동, 1이면 벽을 부쉈는지 체크 -> 안 부쉈다면 부수고 이동
"""

def solve():
    from collections import deque
    N, M = map(int, input().split())
    # graph = [list(map(int, input().split())) for _ in range(N)] # IndexError
    graph = [list(map(int, input().strip())) for _ in range(N)]

    visited = [[[-1]*2 for _ in range(M)] for _ in range(N)] # visited[y][x][0]: 벽을 부수지 않고 도달한 거리, visited[y][x][1]: 벽을 부수고 도달한 거리

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    dq = deque([(0,0,0,1)]) #(y, x, 벽부숨여부, 거리) - 0이면 안 부심, 1이면 부심
    visited[0][0][0] = 1 # 시작하는 칸 포함

    while dq:
        y, x, wall, dist = dq.popleft()
        if y == N-1 and x == M-1: # 도착점
            return dist
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                # 벽 아니고, 방문 안한 경우
                if graph[ny][nx]==0 and visited[ny][nx][wall]==-1:
                    visited[ny][nx][wall] = dist+1
                    dq.append((ny, nx, wall, dist+1))
                # 벽이고, 아직 부수지 않은 경우
                elif graph[ny][nx]==1 and wall==0 and visited[ny][nx][1]==-1:
                    visited[ny][nx][1] = dist+1
                    dq.append((ny, nx, 1, dist+1))
    return -1

if __name__=='__main__':
    result = solve()
    print(result)

"""
PyPy3
메모리 : 299484 KB
시간 : 1608 ms
"""