def find_x (arr) :
    if arr[0] == "x" :
        return 0
    return find_x (arr[1:]) + 1

arr = input()
print(find_x(arr))