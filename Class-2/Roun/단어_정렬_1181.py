############
# silver 5 #
############

import sys

input = sys.stdin.readline

num = int(input())
words = []

for i in range(num):
    words.append(input().rstrip())

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

print('\n'.join(words))

###################
# memory: 37456KB #
# time:   72ms    #
###################