import sys

input = sys.stdin.readline

def do_command(command: str, value: str = None):
    global stack

    if command == 'push':
        stack.append(value)
        return None
    elif command == 'pop':
        if stack:
            return stack.pop()
        else:
            return -1
    elif command == 'size':
        return len(stack)
    elif command == 'empty':
        if stack:
            return 0
        else:
            return 1
    elif command == 'top':
        if stack:
            return stack[-1]
        else:
            return -1

num = int(input())

stack = []
results = ""

for i in range(num):
    command_line = input().split()

    result = do_command(*command_line)
    if result != None:
        results += str(result) + "\n"

print(results)

###################
# memory: 33432KB #
# time:   48ms    #
###################