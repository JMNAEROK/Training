import string
def find_empty (array) :
    hash_table = {}
    for value in array :
        hash_table[value] = True
    for search in string.ascii_lowercase :
        if (search not in hash_table) :
            return search
    return None
text = str(input())
print(find_empty(text))