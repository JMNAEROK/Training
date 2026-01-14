def find_non_duplication (text) :
    hash_table = {}
    for value in text :
        if (hash_table.get(value)) :
            hash_table[value] += 1
        else :
            hash_table[value] = 1
    for value in text :
        if (hash_table[value] == 1) :
            return value
text = input()
print(find_non_duplication (text))