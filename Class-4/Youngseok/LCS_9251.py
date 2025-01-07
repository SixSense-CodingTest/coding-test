str1 = input()
str2 = input()
dp = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]
res = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]: dp[j][i] = dp[j-1][i-1] + 1
        else: dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        res = max(res, dp[j][i])
print(res)
# 57628kb
# 572ms

str1 = input()
str2 = input()
dp = [0] * (len(str2)+1)
for i in range(len(str1)):
    tmp = dp.copy()
    for j in range(len(str2)):
        if str1[i] == str2[j]: dp[j] = tmp[j-1]+1
        else: dp[j] = max(tmp[j], dp[j-1])
print(dp[j])
# 32412kb
# 312ms

str1 = input()
str2 = input()
dp = [0] * (len(str2)+1)
for i in str1:
    tmp = 0
    for j in range(len(str2)):
        if tmp < dp[j]: tmp = dp[j]
        elif i == str2[j]: dp[j] = tmp+1
print(max(dp))
# 32412kb
# 192ms