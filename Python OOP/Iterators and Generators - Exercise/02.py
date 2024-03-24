class dictionary_iter:
    def __init__(self, dict) -> None:
        self.dict = dict
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < len(self.dict):
            resustl = self.i
            self.i += 1
            return list(self.dict.items())[resustl]
        
        else:
            raise StopIteration()
    


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
