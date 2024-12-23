##########
# gold 5 #
##########

import sys
from collections import deque

input = sys.stdin.readline

def print_queue(items: deque) -> None:
    output = "[" + ",".join(items) + "]\n"
    sys.stdout.write(output)


def solve(commands: str, number_of_items: int, items: deque) -> bool:
    reversed_flag = False  # 역순 관리

    for command in commands:
        if command == 'R':
            reversed_flag = not reversed_flag  # 역순 플래그 변경
        elif command == 'D':
            if items:
                if reversed_flag:
                    items.pop()  # 역순이라면 뒤에서 제거
                else:
                    items.popleft()  # 순서대로라면 앞에서 제거
            else:
                return False

    if reversed_flag:
        items.reverse()  # 최종적으로 한 번만 뒤집음

    print_queue(items)
    return True

number_of_case = int(input())

for i in range(number_of_case):
    commands = input().rstrip()
    number_of_items = int(input())
    if number_of_items == 0:
        input()
        items = deque()
    else:
        items = deque(input().strip()[1:-1].split(','))

    if not solve(commands, number_of_items, items):
        sys.stdout.write("error\n")

###################
# memory: 41828KB #
# time:   116ms   #
###################

# 파싱 문제
# R을 여러번 처리할 필요가 없음 (R은 O(N)의 시간이 소요)
# R을 플래그로 설정해서, 플래그에 따라 D를 수행함 (앞에서 빼거나, 뒤에서 빼거나)
# 마지막 R 플래그를 활용해서 reverse를 한 번만 수행