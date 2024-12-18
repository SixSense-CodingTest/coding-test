import sys
from collections import Counter

input = sys.stdin.readline

_ = int(input())
storage = Counter(map(int, input().split()))

_ = int(input())
target = list(map(int, input().split()))

for item in target:
    print(storage.get(item, 0), end=" ")

####################
# memory: 124940KB #
# time:   832ms    #
####################