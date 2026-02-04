# class Node :
#     def __init__ (self, data) :
#         self.data = data
#         self.next_node = None
#         self.previous_node = None

# class DoublyLinkedList :
#     def __init__ (self, first_node = None, last_node = None) :
#         self.first_node = first_node
#         self.last_node = last_node
        
#     def append (self, value) :
#         new_node = Node(value)

#         if not self.first_node :
#             self.first_node = new_node
#             self.last_node = new_node
#         else :
#             new_node.previous_node = self.last_node
#             self.last_node.next_node = new_node
#             self.last_node = new_node
    
#     def pop_head (self) :
#         popped_node = self.first_node
#         self.first_node = self.first_node.next_node
#         self.first_node.previous_node = None
#         return popped_node
    
#     def print_all_in_reverse (self) :
#         current_node = self.last_node
#         while current_node :
#             print(current_node)
#             current_node = current_node.previous_node
        
class Node :
    def __init__ (self, data) :
        self.data = data
        self.next_node = None

class LinkedList :
    def __init__ (self, first_node = None) :
        self.first_node = first_node

    def read (self, index) :
        current_node = self.first_node
        current_index = 0

        while current_index < index :
            current_node = current_node.next_node
            current_index += 1

            if not current_node :
                return None

        return current_node.data
    
    def search (self, value) :
        current_node = self.first_node
        current_index = 0

        while True :
            if current_node.data == value :
                return current_index
            
            current_node = current_node.next_node

            if not current_node :
                break

            current_index += 1
        
        return None

    def insert (self, index, value) :
        new_node = Node(value)

        if index == 0 :
            new_node.next_node = self.first_node
            self.first_node = new_node
        
        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1) :
            current_node = current_node.next_node
            current_index += 1
        
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete (self, index) :
        if index == 0 :
            self.first_node = self.first_node.next_node
            return
        
        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1) :
            current_node = current_node.next_node
            current_index += 1
        
        node_after_deleted_node = current_node.next_node.next_node

        current_node.next_node = node_after_deleted_node

    def print_all (self) :
        current_node = self.first_node
        while current_node :
            print(current_node.data)
            current_node = current_node.next_node
    
    def return_the_last_value (self) :
        current_node = self.first_node
        while current_node.next_node :
            current_node = current_node.next_node
        return current_node.data
    
    def change_links_in_reverse (self) :
        current_node = self.first_node
        previous_node = None
        while current_node :
            next_node = current_node.next_node
            current_node.next_node = previous_node

            previous_node = current_node
            current_node = next_node
        self.first_node = previous_node
            
def delete_node (node) :
    node.data = node.next_node.data
    node.next_node = node.next_node.next_node


node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

list = LinkedList(node_1)

delete_node (node_2)
list.print_all()

    
    