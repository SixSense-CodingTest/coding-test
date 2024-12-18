N,M = list(map(int,input().split()))

B = []

for _ in range(N):
    B.append(input())

check1 = ['WB'*4,'BW'*4]*4
check2 = ['BW'*4,'WB'*4]*4



def check_str(str1,str2):
    str1 = ''.join(str1)
    str2 = ''.join(str2)

    res = 0 
    for i in range(len(str1)):
        if str1[i]!= str2[i]:
            res+=1

    return res

min_ans = 1e9 

for i in range(N-7):
    for k in range(M-7):
        tmp = [ row[k:k+8] for row in B[i:i+8]]

        min_ans = min(check_str(tmp,check1),check_str(tmp,check2),min_ans)

print(min_ans)