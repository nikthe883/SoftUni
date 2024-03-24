class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count > 0:
            self.count -= 1
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration()


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

