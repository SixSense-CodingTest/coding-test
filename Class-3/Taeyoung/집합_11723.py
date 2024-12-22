import sys

input = sys.stdin.readline

S = set()


def set_add(n):
    S.add(n)


def set_check(n):
    return 1 if n in S else 0


def set_remove(n):
    if set_check(n):
        S.remove(n)


def set_toggle(n):
    if set_check(n):
        S.remove(n)
    else:
        set_add(n)


def set_all():
    global S
    S = {i for i in range(1, 21)}


def set_empty():
    global S
    S = set()


for i in range(int(input().strip())):
    c = input().split()
    if c[0] == 'add':
        set_add(int(c[1]))
    elif c[0] == 'remove':
        set_remove(int(c[1]))
    elif c[0] == 'check':
        print(set_check(int(c[1])))
    elif c[0] == 'toggle':
        set_toggle(int(c[1]))
    elif c[0] == 'all':
        set_all()
    else:
        set_empty()

'''
메모리 : 32412 KB
시간 : 3468 ms
'''
