N, y, x = map(int, input().split())

def rec(N, y, x, T):
    if N == 1:
        return T + 2 * y + x

    size = 2 ** (N - 1)
    quarter_area = size * size

    if y < size and x < size:  # 1
        return rec(N - 1, y, x, T)
    elif y < size and x >= size:  # 2
        return rec(N - 1, y , x - size, T + quarter_area)
    elif y >= size and x < size:  # 3
        return rec(N - 1, y - size, x , T + 2 * quarter_area)
    else:  # 4
        return rec(N - 1, y - size, x - size, T + 3 * quarter_area)

print(rec(N, y, x, 0))