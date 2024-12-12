############
# bronze 1 #
############

import sys

input = sys.stdin.readline

number_of_subjects = int(input())

subjects = list(map(int, input().rstrip().split()))

max_score = max(subjects)

subjects = list(map(lambda x: x / max_score * 100, subjects))

print(sum(subjects) / len(subjects))

###################
# memory: 32412KB #
# time:   40ms    #
###################