# n개의 도시, m개의 버스
# A에서 B로 가는 최소 비용 출력
# 1행 2열 (도시 1에서 도시2 이동 최소비용) 부터 n행 n-1열까지

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

INF = float('inf')

n = int(input())
m = int(input())

price_board = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    price_board[i][i] = 0  # 자기 자신으로 가는 비용은 0

price_dict = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    price_dict[a].append((b, c))

# 다익스트라 알고리즘
def dijkstra(start, price_dict, price_board):
    heap = []
    heapq.heappush(heap, (0, start))  # (비용, 도시)
    visited = [False] * (n + 1)  # 방문 여부 확인

    while heap:
        current_cost, current_city = heapq.heappop(heap)

        if visited[current_city]:
            continue
        visited[current_city] = True

        for next_city, next_cost in price_dict[current_city]:
 
            new_cost = current_cost + next_cost

            if new_cost < price_board[start][next_city]:
                price_board[start][next_city] = new_cost
                heapq.heappush(heap, (new_cost, next_city))

# 각 도시에 대해 다익스트라 알고리즘 적용
for start_city in range(1, n + 1):
    dijkstra(start_city, price_dict, price_board)

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if price_board[i][j] == INF:
            print(0, end=" ")
        else:
            print(price_board[i][j], end=" ")
    print()
        
    


