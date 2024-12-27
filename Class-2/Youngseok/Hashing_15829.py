n, s, res = input(), input(), 0
for i, a in enumerate(s): res += (ord(a)-ord('a')+1)*(31**i)
print(res%1234567891)