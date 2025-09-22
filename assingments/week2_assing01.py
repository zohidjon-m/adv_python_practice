

#assignment 1

length = eval(input("Please, enter the length of rectangular: "))

if not type(length) is int or float:
  raise TypeError("Only integers or float values are allowed")

breadth = eval(input(" Enter the breadth of the rectangular: "))

if not type(breadth) is int or float:
  raise TypeError("Only integers or float values are allowed")

print(f"the area of the rectangular is {length*breadth}")

