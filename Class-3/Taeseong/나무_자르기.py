N, M = list(map(int,input().split()))

woods = list(map(int,input().split()))

def cut_wood(hei):
    # global woods 
    res = 0
    for i in woods:
        if i>hei:
            res+=i-hei
    
    return res 

def bin_search():
    # global woods
    start = 0
    end = max(woods)

    res = -1 
    while start<=end:
        mid = (start+end)//2
        target = cut_wood(mid)
        # print(target,start,end,mid)
        if target > M:
            res = mid 
            start = mid+1
        elif target < M:
            end = mid-1 
        else:
            return mid
        
    return res 

print(bin_search())







