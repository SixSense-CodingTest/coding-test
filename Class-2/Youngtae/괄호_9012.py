# 입력된 괄호 문자열이 올바른지 YES NO로 출력
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    gwalhos = (deque(input().strip()))
    stack = deque()

    is_vps = True
    while gwalhos:
        gwalho = gwalhos.popleft() 
        if gwalho == '(':
            stack.append(gwalho)  
        else: 
            if stack:
                stack.pop() 
            else:
                is_vps = False
                break

    if is_vps and not stack:
        print("YES")
    else:
        print("NO")



