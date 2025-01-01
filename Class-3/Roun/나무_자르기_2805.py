############
# silver 2 #
############

import sys

input = sys.stdin.readline

number_of_trees, target_height = map(int, input().split())

trees = list(map(int, input().split()))

left, right = 0, max(trees)
result = 0

# binary search
while left <= right:
    mid = (left + right) // 2

    height = sum(map(lambda x: x - mid if x >= mid else 0, trees))

    if height >= target_height:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)

####################
# memory: 148224KB #
# time:   2780ms   #
####################