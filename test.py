def fibonacci (N) :
    if hash.get(N) is None :
        hash[N] = fibonacci(N-1) + fibonacci(N-2)
    return hash[N]
N = int(input())
hash = {0 : 0, 1 : 1}
print(fibonacci(N))
