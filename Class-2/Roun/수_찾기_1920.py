############
# silver 4 #
############

import sys

input = sys.stdin.readline

_ = int(input())
storage = set(map(int, input().split()))

storage = {item: True for item in storage}

_ = int(input())
target = list(map(int, input().split()))

for item in target:
    try:
        storage[item]
        print(1)
    except:
        print(0)

###################
# memory: 52832KB #
# time:   160ms   #
###################