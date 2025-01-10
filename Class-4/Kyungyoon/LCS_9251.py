input1 = input()
input2 = input()

dp = [[0] * (len(input2) + 1) for _ in range(len(input1) + 1)] # 빈문자열 포함 행렬생성

for i in range(1, len(input1) + 1):
    for j in range(1, len(input2) + 1):
        if input1[i - 1] == input2[j - 1]:  # 문자가 같을때
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 다를때
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # max(위, 왼쪽)

print(dp[len(input1)][len(input2)]) 

"""
PyPy3
메모리 : 118524 KB
시간 : 120 ms
"""