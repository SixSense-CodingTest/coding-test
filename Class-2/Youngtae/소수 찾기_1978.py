def is_sosu(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


N = int(input())
numbers = map(int, input().split())
count_sosu = 0

for number in numbers:
    if is_sosu(number):
        count_sosu += 1

print(count_sosu)


