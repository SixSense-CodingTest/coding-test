while True:
    
    lens = list(map(int,input().split()))
    
    if lens == [0,0,0]:
        break
    
    lens.sort()
    
    if lens[0]**2 + lens[1]**2 == lens[2]**2:
        print("right")
    else:
        print("wrong")