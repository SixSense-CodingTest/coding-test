while True:
    temp = input()

    if temp == "0 0 0":
        break
    
    temp = list(map(int, temp.split()))
    max_temp = max(temp)
    min_temp = min(temp)

    if max_temp**2 - min_temp**2 == (sum(temp)-max_temp-min_temp)**2:
        print("right")
    else:
        print("wrong")