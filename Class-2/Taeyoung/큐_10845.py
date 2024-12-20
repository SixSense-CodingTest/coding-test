import sys
input = sys.stdin.readline

q = []

N = int(input().strip())


def q_empty():
    return 1 if len(q) == 0 else 0


def q_size():
    return len(q)


def q_push(n):
    q.append(n)


def q_front():
    return -1 if q_empty() else q[0]


def q_back():
    return -1 if q_empty() else q[-1]


def q_pop():
    return -1 if q_empty() else q.pop(0)


for _ in range(N):
    command = input().strip()
    if "push" in command:
        q_push(int(command.split()[1]))
    elif command == "front":
        print(q_front())
    elif command == "back":
        print(q_back())
    elif command == "size":
        print(q_size())
    elif command == "empty":
        print(q_empty())
    elif command == "pop":
        print(q_pop())

'''
메모리 : 33432 KB
시간 : 44 ms
'''
