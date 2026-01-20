def compression (x, y, n) :
    first = array[x][y]
    same = True
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if first != array[i][j] :
                same = False
                break
    if same :
        return first
    half = n // 2
    return "(" + \
        compression(x, y, half) + \
        compression(x, y+half, half) + \
        compression(x+half, y, half) + \
        compression(x+half, y+half, half) + \
         ")"

N = int(input())
array = list(input().strip() for i in range(N))
print(array)
print(compression(0, 0, N))
