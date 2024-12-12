while True:
    a,b,c = map(int, input().split())
    if a == b == c ==0:
        break
    num_sum = a + b + c
    largest = max(a,b,c)
    shortest = min(a,b,c)
    remain = num_sum - largest - shortest

    if largest**2 - shortest**2 == remain **2:
        print("right")
    else:
        print("wrong")