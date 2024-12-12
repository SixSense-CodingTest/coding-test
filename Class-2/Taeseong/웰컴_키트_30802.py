N = int(input())
Ts = list(map(int,input().split()))
T,P = list(map(int,input().split()))

T_sum = 0

for i in Ts:
    tmp = 0 if i%T==0 else 1 
    T_sum+= (i//T + tmp)


print(T_sum)
print(N//P ,N%P )