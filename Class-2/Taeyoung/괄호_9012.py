import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    stack = []
    flag = True

    for j in input():
        if j == '(':
            stack.append(j)
        elif j == ')':
            if j == ')' and len(stack) == 0:
                flag = False
                break
            stack.pop()

    if flag and len(stack) == 0:
        print("YES")
    else:
        print("NO")

'''
메모리 : 32412 KB
시간 : 40 ms
'''
