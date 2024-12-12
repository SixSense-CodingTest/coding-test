N = int(input())
Ns = list(map(int,input().split()))


sosu = [] 

for i in range(2,1001):
    flag = 0 
    for k in sosu:
        if i%k==0:
            flag=1 
            break 
    if flag == 0:
        sosu.append(i)

cnt = 0
for i in Ns:
    if i in sosu:
        cnt+=1

print(cnt)

