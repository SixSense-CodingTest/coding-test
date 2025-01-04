"""
백트래킹 : 조건을 만족하는 경로만 탐색하기 위해 가지치기를 포함하는 탐색기법(해를 찾는 과정에서 가능성이 없는 경로를 제거)
    - 해를 구하기 위한 탐색
    - N과 M의 문제, 순열조합문제 등
DFS : 모든 경로를 탐색하는 단순 탐색 기법
    - 그래프의 모든 노드를 탐색할 때
"""
# combination 사용해서 푼 방법
from itertools import combinations
N, M = map(int, input().split())
for c in combinations(range(1,N+1), M):
    print(*c)
"""
PyPy3
메모리 : 108384 KB
시간 : 92 ms
"""

# 백트래킹 사용해서 푼 방법(공부용)
N, M = map(int, input().split())
stack = [(1, [])] # (시작숫자, 현재까지의 수열)
while stack:
    start, sequence = stack.pop()

    # 가지치기 - 종료조건
    if len(sequence) == M:
        print(*sequence)
        continue
    
    # 가지치기 - 오름차순 유지(start보다 작은 숫자 탐색하지않음)
    for i in range(N, start-1, -1): 
        stack.append((i+1, sequence + [i]))

"""
예시(N=3, M=2)
시작 상태 : stack = [(1, [])]
1단계 : stack = [(4, [3]), (3, [2]), (2, [1])]
2단계 : stack = [(4, [3]), (3, [2]), (4, [1, 3]), (3, [1, 2])]
3단계 : 3, [1, 2] 가 종료조건에 부합 -> continue
stack = [(4, [3]), (3, [2]), (4, [1, 3])]
"""

"""
PyPy3
메모리 : 108384 KB
시간 : 96 ms
"""