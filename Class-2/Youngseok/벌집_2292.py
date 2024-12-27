n = int(input())
l, res = 1, 1
while l<n: l, res = l+res*6, res+1
print(res)