from collections import deque

class vowels:
    VOWELS = "aeiouy"
    def __init__(self,thing):
        self.thing = thing
        self.vowels = deque([x for x in thing if x.lower() in vowels.VOWELS])

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.vowels:
            raise StopIteration

        return self.vowels.popleft()
