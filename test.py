import string
class stack :
    def __init__ (self) :
        self.data = []
    def push (self, text) :
        self.data.append(text)
    def pop (self) :
        if (len(self.data) == 0) :
            return None
        return self.data.pop()
    def read (self) :
        if (len(self.data) == 0) :
            return None
        return self.data[-1]
priority = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
expression = input()
operator = stack()
for value in expression :
    if (value in string.ascii_uppercase) :
        print(value, end="")
    elif (value == '(') :
        operator.push(value)
    elif (value == ')') :
        while (operator.read() != '(') :
            print(operator.pop(), end="")
        operator.pop()
    else :
        while (operator.read() is not None and operator.read() != '(' and priority[operator.read()] >= priority[value]) :
            print(operator.pop(), end = "")
        operator.push(value)
while(operator.read() is not None) :
    print(operator.pop(), end = "")

