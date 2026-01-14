def find_duplication(array) :
    hash_table = {}
    for value in array :
        if (hash_table.get(value) == True) :
            return value
        else :
            hash_table[value] = True

arr = list(map(str, input().split()))
print(find_duplication(arr))