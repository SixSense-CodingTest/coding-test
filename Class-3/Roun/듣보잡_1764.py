############
# silver 4 #
############

import sys

input = sys.stdin.readline

number_of_listen, number_of_see = map(int, input().split())

listen = set()
see = set()

for i in range(number_of_listen):
    listen.add(input().rstrip())

for i in range(number_of_see):
    see.add(input().rstrip())

intersection = listen.intersection(see)

print(len(intersection))
for item in sorted(intersection):
    print(item)

###################
# memory: 43168KB #
# time:   80ms    #
###################