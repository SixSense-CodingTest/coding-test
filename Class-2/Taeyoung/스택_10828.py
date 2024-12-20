import sys

N = int(sys.stdin.readline())
stack = []

def stack_push(num):
    stack.append(num)

def stack_pop():
    if stack_empty():
        return -1
    else:
        return stack.pop()
    
def stack_size():
    return len(stack)
    
def stack_empty():
    return stack_size() == 0
    
def stack_top():
    if stack_empty():
        return -1
    else:
        return stack[-1]

for _ in range(N):
    command = sys.stdin.readline()
    if 'push' in command:
        stack_push(int(command.split()[1]))
    elif 'top' in command:
        print(stack_top())
    elif 'size' in command:
        print(stack_size())
    elif 'empty' in command:
        print(int(stack_empty()))
    else:
        print(stack_pop())

'''
메모리 : 33432 KB
시간 : 44 ms
'''