n, nlist = input(), set(input().split())
m = input()
res = '\n'.join(['1' if num in nlist else '0' for num in input().split()])
print(res)
# 52264kb
# 88ms