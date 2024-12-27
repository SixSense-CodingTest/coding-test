n = int(input())
if n%5 == 0: print(n//5)
elif n%5 == 1: print(2+(n-6)//5)
elif n%5 == 2: print(4+(n-12)//5 if n > 11 else -1)
elif n%5 == 3: print(1+(n-3)//5)
elif n%5 == 4: print(3+(n-9)//5 if n > 8 else -1)
# 32412kb
# 40ms