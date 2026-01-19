def draw(x, y, n) :
    if n == 1 :
        array[x][y] = "*"
        return
    
    size = n // 3
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            draw(x + i*size, y + j*size, size)

N = int(input())
array = [[" "]*N for _ in range(N)]
draw(0, 0, N)
for i in range(N) :
    for j in range(N) :
        print(array[i][j], end="")
    print()