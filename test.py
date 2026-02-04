class Node :
    def __init__ (self, data) :
        self.data = data
        self.next_node = None
        self.previous_node = None

class DoublyLinkedList :
    def __init__ (self, first_node = None, last_node = None) :
        self.first_node = first_node
        self.last_node = last_node
        
    def append (self, value) :
        new_node = Node(value)

        if not self.first_node :
            self.first_node = new_node
            self.last_node = new_node
        else :
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
    
    def pop_head (self) :
        popped_node = self.first_node
        self.first_node = self.first_node.next_node
        self.first_node.previous_node = None
        return popped_node
    
class Queue :
    def __init__ (self) :
        self.data = DoublyLinkedList()
    
    def enqueue (self, element) :
        self.data.append(element)

    def dequeue (self) :
        dequeued_node = self.data.pop_head()
        return dequeued_node.data
    
    def read (self) :
        if not self.data.first_node :
            return None
        return self.data.first_node.data

