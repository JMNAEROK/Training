def intersection (array1, array2) :
    array3 = list()
    hash_table = {}
    for key in array1 :
        hash_table[key] = True
    for search_value in array2 :
        if (search_value in hash_table) :
            array3.append(search_value)
    return array3
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(intersection(arr1, arr2))