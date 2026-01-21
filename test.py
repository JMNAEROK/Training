def stair_case (N) :
    if (N == 0) : return 1
    if (N < 0) : return 0
    return stair_case(N-1) + stair_case(N-2) + stair_case(N-3)

N = int(input())
print(stair_case(N))