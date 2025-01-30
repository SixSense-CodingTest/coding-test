"""
벨만포드
가중그래프에서 단일 시작점 최단 경로를 찾는 알고리즘
다익스트라와 비슷한 목적을 갖지만, 음의 가중치 간선이 포함된 그래프에서도 동작할 수 있다

특징
입력조건은, 방향그래프 or 무방향 그래프, 간선 가중치는 음수 or 양수
그래프에 음수사이클이 포함되어 있다면, 해당 경로의 최단 경로는 정의되지 않음 - 벨만포드는 이를 탐지 가능

작동원리
시작노드에서 거리는 0으로 설정
나머지 모든 노드의 거리는 무한대로 초기화
최단거리 찾기 : 모든 간선을 최대 V-1번 반복적으로 확인하며 업데이트, 간선 완화 과정에서 더 짧은 경로가 발견되면 경로 업데이트
음수 사이클 확인 : V-1번 완화 이후에도 거리 값이 여전히 줄어드는 간선이 있다면, 음수 사이클이 존재한다고 판정
"""

"""
문제 설명
- N개의 노드, M개의 양방향 간선(2개의 단방향 간선으로 간주), W개의 단방향 간선
- 간선의 개수 : 2M + W
- 도로의 가중치 > 0
- 웜홀의 가중치 < 0 
"""

"""
벨만포드 vs 플로이드워셜
- 벨만포드
단일시작점 최단거리 : 특정 시작점에서 다른 모든 정점까지의 최단거리계산
인접리스트 기반으로 작업하므로, 동일한 두 정점간 도로가 여러개가 있다면, 모든 간선을 따로 처리함 - 최단거리 자동갱신
노드, 간선만 저장
단, 음수사이클 탐지 문제에서는, 시작점에서 접근할 수 없는 정점이 있거나, 그 정점에서 발생하는 음수사이클이 있다면 해당 사이클은 탐지하지 못 하므로
가상의 시작점을 추가해야함

- 플로이드워셜
모든 정점 쌍 간의 최단거리
그래프의 인접행렬로 작업하므로, 동일한 두 정점간 도로가 여러개가 있다면, 가장 작은 가중치만을 사용하여 초기화 - 별도처리필요
모든 노드 쌍 저장
"""
def solve():
    import sys
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        N, M, W = map(int, input().strip().split())

        edges = [] # 간선정보저장
        for _ in range(M):
            S, E, T = map(int, input().strip().split())
            edges.append((S,E,T))
            edges.append((E,S,T))
        for _ in range(W):
            S, E, T = map(int, input().strip().split())
            edges.append((S,E,-T))

        # 가상의 시작점 추가
        for i in range(1, N+1):
            edges.append((0,i,0)) # 모든 기존 정점에 연결

        dist = [float('inf')]*(N+1)
        dist[0] = 0

        # N번 : 벨만포드에서는 N-1번만 간선완화를 수행하지만, 음수사이클을 탐지하기 위한 트릭
        for _ in range(N):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
        
        # 음수 사이클 체크
        flag = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u]+w < dist[v]:
                flag = True # 거리 갱신이 발생 → 음수 사이클 존재
                break
        if flag:
            print('YES')
        else:
            print('NO')
solve()

"""
PyPy3
메모리 : 113480 KB
시간 : 832 ms
"""