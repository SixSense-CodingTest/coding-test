############
# silver 2 #
############

import heapq
import sys

input = sys.stdin.readline

number_of_commands = int(input())
min_heap = []

for i in range(number_of_commands):
    temp = int(input())

    if temp > 0:
        heapq.heappush(min_heap, temp)
    elif temp == 0:
        print(heapq.heappop(min_heap)) if min_heap else print(0)
        
###################
# memory: 38340KB #
# time:   104ms   #
###################