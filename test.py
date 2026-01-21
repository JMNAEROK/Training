def recursion(x, y, N) :
    cn1, cp0, cp1 = 0, 0, 0
    first = array[x][y]
    same = True
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if array[i][j] != first :
                same = False
                break
        if same is False :
            break
    if same is True :
        if (first == -1) : return 1, 0, 0
        if (first == 0) : return 0, 1, 0
        if (first == 1) : return 0, 0, 1

    size = N // 3
    for i in range(3) :
        for j in range(3) :
            a, b, c = recursion(x+size*i, y+size*j, size)
            cn1 += a
            cp0 += b
            cp1 += c
    return cn1, cp0, cp1

    

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

cn1, cp0, cp1 = recursion(0, 0, N)
print(cn1)
print(cp0)
print(cp1)