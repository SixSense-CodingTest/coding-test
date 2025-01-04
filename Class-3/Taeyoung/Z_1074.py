import sys
input = sys.stdin.readline

def z(n, r, c):
    result = 0
    size = 2**n

    while size > 1:
        size //= 2
        if r < size and c < size: # 2사분면
            continue
        elif r < size and c >= size: # 1사분면
            result += size**2
            c -= size
        elif r >= size and c < size: # 3사분면
            result += 2 * size**2
            r -= size
        else:
            result += 3 * size**2 # 4사분면
            c -= size
            r -= size
    return result

N, r, c = map(int, input().split())
print(z(N, r, c))