class Node :
    def __init__ (self, data) :
        self.index = None
        self.data = data
        self.previous_node = None
        self.next_node = None

class DoublelyLinkedList :
    def __init__ (self) :
        first_node = None
        last_node = None
    
N = int(input())
int_array = list(map(int, input().split()))
node_array = []
for index, value in enumerate(int_array) :
    node_array.append(Node(value))
    node_array[index].index = index + 1

#노드 연결
for index in range(len(node_array)) :
    if index == len(node_array) - 1 :
        node_array[index].previous_node = node_array[index - 1]
        node_array[index].next_node = node_array[0]
    else :
        node_array[index].previous_node = node_array[index - 1]
        node_array[index].next_node = node_array[index + 1]
first_node = node_array[0]
last_node = node_array[-1]

ans = []
current_node = node_array[0]
for i in range(N) :
    #인덱스 추가
    ans.append(str(current_node.index))
    move= current_node.data
    #삭제
    temp_prev_node = current_node.previous_node
    temp_next_node = current_node.next_node
    temp_prev_node.next_node = temp_next_node
    temp_next_node.previous_node = temp_prev_node
    
    #
    
    if move > 0 :
        current_node = temp_next_node
        for j in range(move - 1) :
            current_node = current_node.next_node
    elif move < 0 :
        current_node = temp_prev_node
        for j in range(abs(move) - 1) :
            current_node = current_node.previous_node
    

print(" ".join(ans))