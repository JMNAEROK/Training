def anagram (string) :
    if len(string) == 1 :
        return [string[0]]
    collection = []

    substring_anagrams = anagram(string[1:])
    for substring_anagram in substring_anagrams :
        for index in range(len(substring_anagram) + 1) :
            new_string = (substring_anagram[:index]
                              + string[0]
                              + substring_anagram[index:])
            collection.append(new_string)
    return collection

print(anagram(input()))