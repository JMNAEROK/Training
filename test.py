def has_duplicate_value (array) :
    array.sort()
    
    for index in range(len(array) - 1) :
        if array[index] == array[index + 1] :
            return True
    
    return False