# 배열에 자연수 x 넣고
# 가장 작은 값 출력 후 제거
# 처음은 빈 배열에서 시작

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
        


