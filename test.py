N, k = map(int, input().split())
score = list(map(int, input().split()))

for i in range(len(score) - 1) :
    biggest_num_index = i
    for j in range(i+1, len(score)) :
        if(score[biggest_num_index] < score[j]) :
            biggest_num_index = j
    if (biggest_num_index != i) :
        score[i], score[biggest_num_index] = score[biggest_num_index], score[i]

print(score[k-1])