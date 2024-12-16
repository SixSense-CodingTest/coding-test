############
# silver 5 #
############

import sys

input = sys.stdin.readline

num = int(input())

people = []
result = ""

for i in range(num):
    age, name = input().split()
    age = int(age)

    people.append((age, name))

people.sort(key=lambda x: x[0])

for age, name in people:
    result += f"{age} {name}\n"

print(result)

###################
# memory: 46252KB #
# time:   1416ms  #
###################