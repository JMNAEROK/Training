N = int(input())
time = list(map(int, input().split()))

for index in range(1, len(time)) :
    temp_value = time[index]
    position = index - 1
    while(position >= 0) :
        if(time[position] > temp_value) :
            time[position + 1] = time[position]
            position -= 1
        else :
            break
    time[position + 1] = temp_value
print(time)

total_time = 0
for i in range(len(time)) :
    sum = 0
    for j in range(i + 1) :
        sum += time[j]
    total_time += sum

print(total_time)