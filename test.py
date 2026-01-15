class Stack :
    def  __init__ (self) :
        self.data = []
    def push (self, element) :
        self.data.append(element)
    def pop (self) :
        if(len(self.data)) > 0 :
            return self.data.pop()
        else :
            return None
    def read (self) :
        if (len(self.data) > 0) :
            return self.data[-1]
        else :
            return None
class Linter :
    def __init__ (self) :
        self.stack = Stack()
    def lint(self, text) :
        while (self.stack.read()) :
            self.stack.pop()
        matching_braces = {"(" : ")", "{" : "}", "[" : "]"}
        for char in text :
            if char in matching_braces.keys() :
                self.stack.push(char)
            elif char in matching_braces.values() :
                if not self.stack.read() :
                    return char + " 여는 괄호가 없음"
                else :
                    popped_opening_brace = self.stack.pop()
                    if (char != matching_braces.get(popped_opening_brace)) :
                        return char + " 일치하지 않는 유형의 여는 괄호가 있음"
        if (self.stack.read()) :
            return self.stack.read() + " 닫는 괄호가 없음"
        return True
X = Linter()
text = input()
print(X.lint(text))