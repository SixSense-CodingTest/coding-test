############
# silver 4 #
############

import sys

input = sys.stdin.readline

num = int(input())
times = list(map(int, input().split()))

times.sort()

times = [sum(times[:i+1]) for i in range(len(times))]

print(sum(times))

###################
# memory: 32544KB #
# time:   40ms    #
###################