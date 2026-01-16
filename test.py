# class Queue :
#     def __init__ (self) :
#         self.data = []
#     def enqueue(self, element) :
#         self.data.append(element)
#     def dequeue(self) :
#         if len(self.data) > 0 :
#             return self.data.pop(0)
#         else :
#             return None
#     def read(self) :
#         if len(self.data) > 0 :
#             return self.data[0]
#         else :
#             return None
# class PrintManager :
#     def __init__(self) :
#         self.Q = Queue()
#     def queue_print_job(self, document) :
#         self.Q.enqueue(document)
#     def run (self) :
#         while self.Q.read() :
#             self.print_document(self.Q.dequeue())
#     def print_document(self, document) :
#         print(document)
# print_manager = PrintManager()
# print_manager.queue_print_job("First Document")
# print_manager.queue_print_job("Second Document")
# print_manager.queue_print_job("Third Document")
# print_manager.run()

class stack :
    def __init__(self) :
        self.data = []
    def push(self, element) :
        self.data.append(element)
    def read(self) :
        if len(self.data) > 0 :
            return self.data[-1]
        else :
            return None
    def pop(self) :
        if len(self.data) > 0 :
            return self.data.pop()
        else :
            return None
def reverse (arr) :
    while arr.read() :
        print(arr.pop(), end="")
arr = stack()
x = input()
for value in x :
    arr.push(value)
reverse(arr)