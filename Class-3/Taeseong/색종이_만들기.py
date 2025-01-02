N = int(input())

paper = [] 

for _ in range(N):
    paper.append(list(map(int,input().split())))

stack = []

def sum_all(L):
    res = 0
    for i in range(len(L)):
        res+=sum(L[i])
    return res 

stack.append(paper)

white_blue = [0,0]
while stack:
    
    P = stack.pop()
    cnt = sum_all(P)

    if cnt==len(P)*len(P):
        white_blue[1]+=1
        continue 
    elif cnt == 0:
        white_blue[0]+=1
        continue
    else: 
        stack.append([row[:len(P)//2] for row in P[:len(P)//2]])
        stack.append([row[len(P)//2:] for row in P[:len(P)//2]])
        stack.append([row[:len(P)//2] for row in P[len(P)//2:]])
        stack.append([row[len(P)//2:] for row in P[len(P)//2:]])

print(white_blue[0])
print(white_blue[1])
