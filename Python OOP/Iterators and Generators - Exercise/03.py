class countdown_iterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n >= 0:
            result = self.n
            self.n -= 1
            return result
        else:
            raise StopIteration()
        

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
