
class even_iterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while(self.index < len(self.lst)):
            if self.lst[self.index] % 2 == 0:
                i = self.lst[self.index]
                self.index +=1
                return i
            else:
                self.index +=1
        raise StopIteration

it = even_iterator([2,3,4,5,6,76,4,98,452,0,32])
# for i in it:
#     print(i)

i = next(it)
print(i)