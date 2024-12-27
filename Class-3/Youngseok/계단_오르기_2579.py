dp = [(0,0),(0,0)]
for _ in range(int(input())):
    i = int(input())
    dp.append((dp[-1][1]+i,max(dp[-2])+i))
print(max(dp[-1]))
# 32412kb
# 36ms