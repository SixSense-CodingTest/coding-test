n = int(input())
a, b = 1, 1
for i in range(n): a, b = b, a+b
print(a%10007)
# 32412kb
# 40ms

a, b = 1, 1
for i in range(int(input())): a, b = b, a+b
print(a%10007)
# 32412kb
# 40ms