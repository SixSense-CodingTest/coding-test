############
# silver 5 #
############

from collections import deque
import sys

input = sys.stdin.readline

queue = deque()

def do_command(command: str, value: str = None):
    global queue

    if command == "push":
        queue.append(value)
    elif command == "pop":
        print(queue.popleft()) if queue else print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        print(0) if queue else print(1)
    elif command == "front":
        print(queue[0]) if queue else print(-1)
    elif command == "back":
        print(queue[-1]) if queue else print(-1)

num = int(input())

for i in range(num):
    command_line = input().split()

    do_command(*command_line)

###################
# memory: 34924KB #
# time:   64ms    #
###################