arr = [0] * 10
for i in range(10) :
    arr[i] = int(input())
for i in range(len(arr)) :
    arr[i] %= 42
test = [0 for i in range(42)]
for value in arr :
    test[value] += 1

count = 0
for i in range(len(test)) :
    if (test[i] >= 1) :
        count += 1

print(count)