
class Stack:

    def __init__(self) -> None:
        self.data = []

    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False
    
    def __str__(self) -> str:
         return '[' + ', '.join(self.data[::-1]) + ']'
    
stack = Stack()
stack.push("apple")
stack.push("carrot")
stack.top()
print(stack)