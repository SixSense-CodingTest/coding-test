u, d, g = map(int, input().split())
print((g-u)//(u-d)+1 if (g-u)%(u-d)==0 else (g-u)//(u-d)+2)