def num_ch (arr) :
    if not arr :
        return 0
    n = len(arr[0])
    return n + num_ch(arr[1:])

array = input().split()
print(num_ch(array))