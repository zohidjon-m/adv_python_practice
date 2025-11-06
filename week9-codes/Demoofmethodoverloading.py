######################Demo of method overloading######################

# class math:
#     def add(self, a, b):
#         return a + b
#     def add(self, a, b, c):
#         return a + b + c
# m = math()
# print(m.add(2, 3, 4))  # Calls the last defined add method
# print(m.add(2,3))     # This will raise an error

######################Correct way to achieve method overloading (*arg)######################
#args is a tuple

#It collects all positional arguments

class Math:
    def add(self, *args, **kwargs):
        print("Positional args:", args)
        print("Keyword args:", kwargs)

        total = sum(args)

        for key, value in kwargs.items():
            total += value

        return total


m = Math()
print(m.add(1, 2, 3))  
print(m.add(a=4, b=5)) 
print(m.add(1, 2, x=10, y=20))

print(m.add(1, 2, 3, 4))  # 10
