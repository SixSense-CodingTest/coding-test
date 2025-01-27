# N개의 숫자로 구분된 각 마을에 한명씩 학생
# N명의 학생이 X번마을에서 파티
# 마을 사이 M개의 단방향 도로, i번째 길 지나느데 T_i만큼 시간 소비
# 각 학생은 최단경로로 X번마을에 오고가는 시간 측정
# 그 중에 최장시간 출력

import heapq
from collections import defaultdict
import sys

input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v, t = map(int, input().split())  # u: 시작점, v: 도착점, t: 소요 시간
    graph[u].append((v, t))

def dijkstra(start):
    times = [INF] * (N + 1)
    times[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_time, current_node = heapq.heappop(pq)
        
        if current_time > times[current_node]:
            continue
        
        for neighbor, time_needed in graph[current_node]:
            new_time = current_time + time_needed
            if new_time < times[neighbor]:
                times[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    
    return times

time_from_x = dijkstra(X)

max_time = 0
for i in range(1, N + 1):
    time_to_x = dijkstra(i)
    round_trip_time = time_to_x[X] + time_from_x[i]
    max_time = max(max_time, round_trip_time)

print(max_time)




        


