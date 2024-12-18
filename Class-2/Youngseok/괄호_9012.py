n = int(input())
for i in range(n):
    o = 0
    for j in input():
        if j == '(': o += 1
        else: 
            o -= 1
            if o < 0: 
                print('NO')
                break
    else: 
        if o: print('NO')
        else: print('YES')
# 32412kb
# 44ms

n = int(input())
for i in range(n):
    o = 0
    for j in input():
        if j == '(': o += 1
        else: 
            o -= 1
            if o < 0: break
    if o: print('NO')
    else: print('YES')
# 32412kb
# 48ms # if 문을 무조건 한번 더 써야돼서 좀 더 느려진듯

n = int(input())
for i in range(n):
    s = input()
    while '()' in s: s = s.replace('()','')
    print('NO' if s else 'YES')
# 32412kb
# 48ms