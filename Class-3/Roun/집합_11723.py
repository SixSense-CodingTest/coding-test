############
# silver 5 #
############

import sys

input = sys.stdin.readline

def check(value: str) -> bool:
    global factory
    return True if value in factory else False

def do_command(command: str, value: str = None):
    global factory

    if value:
        value = int(value)

    if command == "add":
        factory.add(value)
    elif command == "remove":
        if check(value):
            factory.remove(value)
    elif command == "check":
        print(1) if check(value) else print(0)
    elif command == "toggle":
        factory.remove(value) if check(value) else factory.add(value)
    elif command == "all":
        factory = set(range(1, 21))
    elif command == "empty":
        factory = set()

factory = set()

num = int(input())

for i in range(num):
    command_line = input().split()

    do_command(*command_line)

###################
# memory: 32412KB #
# time:   2944ms  #
###################