N = int(input())

meating = []

for i in range(N):
    start,end = list(map(int,input().split()))
    meating.append([start,end])

meating.sort(key=lambda x: (x[1],x[0]))

cnt = 0 
end_time = -1 

for s,e in meating:
    if s>=end_time:
        cnt+=1
        end_time=e 

print(cnt)