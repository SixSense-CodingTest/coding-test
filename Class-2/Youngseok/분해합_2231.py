n = input()
l, n = len(n), int(n)
st = max(0, n-10*l)
for i in range(st, n):
    if n == i+sum(map(int,list(str(i)))):
        print(i)
        break
else: print(0)