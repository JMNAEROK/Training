def quickselect (array, left_index, right_index, num) :
    pivot_index = right_index
    right_index -= 1
    
    while True :
        while array[left_index] < array[pivot_index] :
            left_index += 1
        while array[right_index] > array[pivot_index] :
            right_index -= 1
        
        if left_index >= right_index :
            break
        else :
            array[left_index], array[right_index] = \
                array[right_index], array[left_index]
            left_index += 1

    array[left_index], array[pivot_index] = \
        array[pivot_index], array[left_index]
    pivot_index = left_index

    if num < pivot_index :
        return quickselect (array, 0, pivot_index - 1, num)
    elif num > pivot_index :
        return quickselect (array, pivot_index + 1, len(array) - 1, num)
    else :
        return array[pivot_index]

    
N, R = map(int, input().split())
array = list(map(int, input().split()))

print(quickselect(array, 0, len(array) - 1, R))