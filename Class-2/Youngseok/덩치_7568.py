l = [tuple(map(int, input().split())) for _ in range(int(input()))]
for i in l:
    c = 1
    for j in l:
        if i[0] < j[0] and i[1] < j[1]: c+=1
    print(c, end=' ')
# 32412kb
# 36ms