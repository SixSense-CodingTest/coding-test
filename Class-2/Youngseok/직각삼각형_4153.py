a, b, c = sorted(map(int, input().split()))
while a and b and c:
    if a**2+b**2==c**2: print('right')
    else: print('wrong')
    a, b, c = sorted(map(int, input().split()))