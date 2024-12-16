O,T = list(map(int,input().split()))


yak = 1
bae = 10001

i = 1

while min(O,T)>=i:    
    if O%i == 0 and T%i==0:
        yak = i
    i+=1


i = yak 
while True:

    if i%O == 0 and i%T == 0:
        bae = i 
        break
    
    i+=yak 
    

    

print(yak)
print(bae)