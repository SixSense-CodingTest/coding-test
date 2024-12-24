import heapq
h = []
for _ in range(int(input())):
    i = int(input())
    if i: heapq.heappush(h, i)
    elif h: print(heapq.heappop(h))
    else: print(0)
# 38340kb
# 108ms