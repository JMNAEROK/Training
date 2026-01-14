def find_the_same_prefix(phone_num) :
    hash_table = {}
    for i in range(phone_num) :
        hash_table[(input())] = True
    for value in hash_table :
        for j in range(1, len(value)) :
            if(hash_table.get(value[:j]) == True) :
                return "NO"
    return "YES"
test_case_num = int(input())
for i in range(test_case_num) :
    phone_num = int(input())
    print(find_the_same_prefix(phone_num))