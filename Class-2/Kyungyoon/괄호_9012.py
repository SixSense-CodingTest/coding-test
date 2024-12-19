from collections import deque

T = int(input())
str_list = []
for _ in range(T):
    S = input()
    str_list.append(S)

for st in str_list:
    gual = deque() # 한 줄 지날 때마다 gual 초기화
    for s in st:
        if s == '(':
            gual.append(1)
        if s == ')':
            if len(gual) != 0:
                gual.pop()  # pop할 게 없으면 오류남
            else: 
                print('NO') # 길이가 0인데 )면 VPS가 아니므로 NO
                break
    # for문이 break로 안 멈추고 무사히 돌아가야 else 동작
    else:
        if len(gual) == 0:
            print('YES')
        else:
            print('NO')

"""
PyPy3
메모리 : 111312 KB
시간 : 116 ms
"""