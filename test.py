def select_even (arr) :
    if not arr :
        return []
    if arr[0] % 2 == 0 :
        return [arr[0]] + select_even(arr[1:])
    else :
        return select_even(arr[1:])

array = list(map(int, input().split()))
print(select_even (array))