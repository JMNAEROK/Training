def binary_search(search_value, array) :
    lower_point = 0
    upper_point = len(array) - 1
    while (lower_point <= upper_point) :
        mid_point = (lower_point + upper_point) // 2
        if (search_value == array[mid_point]) :
            return 1
        if (search_value < array[mid_point]) :
            upper_point = mid_point - 1
        if (search_value > array[mid_point]) :
            lower_point = mid_point + 1
    return 0

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()
for test_value in B :
    print(binary_search(test_value, A))