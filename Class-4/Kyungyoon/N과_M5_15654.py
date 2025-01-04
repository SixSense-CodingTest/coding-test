"""
백트래킹 : 조건을 만족하는 경로만 탐색하기 위해 가지치기를 포함하는 탐색기법(해를 찾는 과정에서 가능성이 없는 경로를 제거)
    - 해를 구하기 위한 탐색
    - N과 M의 문제, 순열조합문제 등
DFS : 모든 경로를 탐색하는 단순 탐색 기법
    - 그래프의 모든 노드를 탐색할 때
"""
N, M = map(int, input().split())
numbers = sorted(map(int, input().split())) # 1789

visited = [False]*N
result = []
stack = [([], visited[:])] # 초기화 (지금까지 방문한 노드, 방문상태)  

while stack:
    sequence, visited = stack.pop()
    # 가지치기 - 종료조건
    if len(sequence) == M:
        result.append(sequence)
        continue
        
    # 가지치기 - 역순으로 추가하여 사전 순 탐색
    for i in range(N-1, -1, -1): # N-1 : numbers[i] 인덱스 맞추려고
        if not visited[i]:
           new = sequence + [numbers[i]]
           new_visited = visited[:]
           new_visited[i] = True
           stack.append((new, new_visited))

for res in result:
    print(' '.join(map(str, res))) 

"""
stack = [([], [False, False, False, False])] 
stack = [([9], [False, False, False, True]),
         ([8], [False, False, True, False]),
         ([7], [False, True, False, False]),
         ([1], [True, False, False, False])]
stack = [([9], [False, False, False, True]),
         ([8], [False, False, True, False]),
         ([7], [False, True, False, False]),
         ([1, 9], [True, False, False, True]),
         ([1, 8], [True, False, True, False]),
         ([1, 7], [True, True, False, False])]
result = [[1, 7]]
stack = [([9], [False, False, False, True]),
         ([8], [False, False, True, False]),
         ([7], [False, True, False, False]),
         ([1, 9], [True, False, False, True]),
         ([1, 8], [True, False, True, False])]
result = [[1, 7], [1, 8], [1, 9]]
stack = [([9], [False, False, False, True]),
         ([8], [False, False, True, False]),
         ([7], [False, True, False, False])]
"""
"""
PyPy3
메모리 : 117800 KB
시간 : 152 ms
"""

