# 
# 펜

N = int(input())
t_shirt = list(map(int, input().split()))
T, P = map(int, input().split())

cnt = 0
for i in t_shirt:
    if i == 0:
        continue

    if i // T < 1:
        cnt += 1
    elif i % T == 0:
        cnt += i // T
    else:
        cnt += i // T + 1

print(cnt)
print(f'{N//P} {N%P}')