# 두 수 입력 받아 최대공약수 최소공배수 출력

a,b = map(int, input().split())
max_yak = 0

for i in range(1,min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        if i > max_yak: 
            max_yak = i

print(max_yak)
print(a * b // max_yak)
