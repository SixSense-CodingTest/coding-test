############
# silver 1 #
############

import sys

input = sys.stdin.readline

def greedy(schedules: list):
    result = 0
    last_end_time = 0

    for start, end in schedules:
        if start >= last_end_time:
            result += 1
            last_end_time = end
    
    return result



number_of_schedules = int(input())
schedules = []

for i in range(number_of_schedules):
    schedules.append(list(map(int, input().split())))

schedules.sort(key=lambda x: (x[1], x[0]))

print(greedy(schedules=schedules))

###################
# memory: 60360KB #
# time:   264ms   #
###################