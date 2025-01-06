N, M = map(int, input().split())
numbers = sorted(map(int, input().split())) 

visited = [False]*N
result = set() # 중복제거
stack = [([], visited[:])] 

while stack:
    sequence, visited = stack.pop()

    if len(sequence) == M:
        result.add(tuple(sequence)) # 튜플변환 -> set 저장
        continue
        
    for i in range(N-1, -1, -1):
        if not visited[i]:
           new = sequence + [numbers[i]]
           new_visited = visited[:]
           new_visited[i] = True
           stack.append((new, new_visited))

for res in sorted(result):
    print(' '.join(map(str, res))) 

"""
PyPy3
메모리 : 116580 KB
시간 : 152 ms
"""