from itertools import combinations

N,M  = list(map(int,input().split()))

cards = list(map(int,input().split()))
cards.sort()

three = 0 

for i,j,k in combinations(cards,3):
    if i+j+k > three and i+j+k<=M:
        three = i+j+k
    
print(three)