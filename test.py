def triangular_number (N) :
    if N == 1 :
        return 1
    return triangular_number(N - 1) + N
N = int(input())
print(triangular_number(N))