import sys

input = sys.stdin.readline

def is_VPS(target: str):
    stack = []

    for item in target:
        if item == '(':
            stack.append(0)
        # 닫는 괄호이고, stack이 비어있지 않을 때
        elif stack:
            stack.pop()
        # 닫는 괄호인데, stack이 비어있으면 VPS가 아님
        else:
            return "NO"
    
    # 마지막에 stack이 남아있으면 VPS가 아님
    return "NO" if stack else "YES"

num = int(input())
result = ""

for i in range(num):
    target = input().rstrip()

    result += is_VPS(target=target) + "\n"

print(result)

###################
# memory: 32412KB #
# time:   44ms    #
###################

        








