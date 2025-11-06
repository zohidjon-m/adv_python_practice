class Father:
    def skills(self):
        print("Programming, Problem Solving")

class Mother:
    def skills(self):
        print("Artistic, Design Thinking")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        Mother.skills(self)
        print("Creative, Analytical Thinking")

c = Child()
c.skills()
print(Child.__mro__)

