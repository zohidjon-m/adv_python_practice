#Iterators
class Countdown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return self.n
        else:
            raise StopIteration()
        
#Generators
def countdown(n):
    while n > 0:
        n -= 1
        yield n
        
        
c = Countdown(5)
k = countdown(5)

print("Iterator: ")
for i in c:
    print(i)
    
print("genetator: ")
for s in k:
    print(s)