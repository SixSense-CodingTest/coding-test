"""
최소 힙
- 힙의 자료구조의 한 종류
- 완전 이진 트리 구조
    - 이진 트리 : 각 노드가 최대 2개의 자식을 가지는 트리 구조
    - 모든 레벨이 꽉 차야 하고, 마지막 레벨이 꽉 차지 않을 수도 있지만, 이 경우 빈 공간이 오른쪽에만 있어야함
- 삽입(힙 상승)
    - 맨 아래 레벨의 가장 오른쪽에 값을 추가
    - 부모 노드와 비교하며 자리를 바꾸는 과정 반복
- 삭제(힙 하강)
    - 힙의 루트노드(최소값)를 제거하면 빈 자리를 채워야 함
    - 가장 아래 레벨의 가장 오른쪽 값을 루트로 옮김
    - 자식들과 비교하며 적절한 위치로 이동
"""
import sys
import heapq
input = sys.stdin.readline

min_heap = [] # 최소 힙으로 사용할 리스트
results = []

N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if min_heap:
            results.append(heapq.heappop(min_heap))
        else:
            results.append(0)
    else:
        heapq.heappush(min_heap, x)
print(*results, sep='\n')

"""
PyPy3
메모리 : 114716 KB
시간 : 152 ms
"""