# # Create with parentheses
# t1 = (1, 2, 3, 4)
# t2 = ("a", "b", "c", "d")
# t3 = (200, "A", [4, 5], 3.2)
# print(t1)
# print(t2)
# print(t3)
# print(t1[0])      # Accessing elements by index
# print(t2[-1])     # Negative indexing
# print(t3[2][1])   # Accessing nested list element
# print(t1[1:3])    # Slicing (creates a new tuple) 
# print(t2[:2])     # Slicing from start
# print(t3[1:])     # Slicing to end
# print(len(t1))    # Length of the tuple

# #parentheses alone vs parentheses + comma
# empty = ()
# print(empty)
# print(type(empty))
# singleton = 'hello',   # <-- the comma is what matters
# print(type(singleton))
# print(len(singleton))
# print(singleton)
# not_a_tuple = ('hello')  # <-- no comma, so not a tuple
# print(type(not_a_tuple))
# print(not_a_tuple)  # just a string

# x = (42)        # just number 42, not a tuple
# y = (42,)       # tuple with one element
# z = 42,         # also tuple with one element (parentheses optional)
# print(type(x), type(y), type(z))
# print(x, y, z)

# #Which of the following correctly creates a tuple with one element, the number 5?

# x = (5,) #.........

# x = (5)  #.......
#################################
#creating tuples with casting
    # t1 = tuple()               # empty tuple
    # t2 = tuple([1, 2, 3])      # from list
    # t3 = tuple("hello")        # from string
    # print(t1, t2, t3)
    # print(type(t1), type(t2), type(t3))

############################
# #Immutability vs Mutability Inside a Tuple
# t = (200, "A", [4,5], 3.2)
# t[1] = "B"      # ERROR: cannot reassign the slot
# t[2] = [4,5,6]    # ERROR: cannot reassign the slot
# t[2].append(6)    # OK! modifies the inner list
# print(t)
# #The tuple reference can’t change, but if an element is a list, 
# # the list itself can be changed.
# Question: find another case can be modified inside the above  tuple
#Nested tuples
# t2 = (1, 2, (3, 4), 5) 
# print(t2)
# t2[2][0] = 1  # This will raise a TypeError since tuples are immutable, if it was the list, maybe we could modify it but it is tuple.
# print(t2)
#################################################
#Tuple Examples (Reverse, Concatenate, Multiply)

# t1 = ("a","b","c")
# print(t1[::-1]) # reversed copy, tuple unchanged.
# print(t1)       # original tuple unchanged
# t2 = ("a","b","c")
# t3 = t1 + t2
# print(t3)
# t3 = t3 * 4
# print(t3)
#Nested Tuples & Loops
# t4 = ((1,2,3), ("a","b","c"))
# for j in t4:   #Outer loop iterates over the two tuples.
#     for k in j: # Inner loop iterates inside each.
#         print(k, end=" ")
#     print()

################
#Tuple unpacking means taking a tuple (or any iterable) and assigning its elements to multiple variables in one line.

#It’s like “unpacking” the items inside a box directly into separate labeled containers.
#Tuple Unpacking (Destructuring)
# t5 = [1, 2, 3]
# a, b, c = t5
# print(a, b, c)
#Important Rule:
#The number of variables on the left must match the number of elements in the tuple.
# a, *b = t5  # This will raise a ValueError because there are not enough values to unpack
# print(a, b)   # This will also raise an error
#Tuple Unpacking with *
# t6 = (1, 2, 3, 4, 5)
# a, *b = t6
# print(a, b)
# *a, b = t6
# print(a, b) 
# a, *b, c = t6
# print(a, b, c)
# print(type(a), type(b), type(c))
# #The * operator collects multiple elements into a list. 
# #Unpacking isn’t limited to tuples — it works with any iterable (list, set, string, etc.)
#Example:
# student = ("Smith", (95, 88, 92))
# name, (math, science, english) = student
# print(name)
# print(science)

##################################################
#Functions & Tuples (Pass-by-Value Behavior)
# def func1(t):
#     t = t * 2
# t = (1,2,3)
# print(t)
# func1(t)
# print(t)
# # #Tuples as Return Values
# def func2():
#     return (1, 2, 3)    
# x, y, z = func2()
# print(x, y, z)
# x, y = func2()  # This will raise a ValueError because there are not enough values to unpack
# print(x, y)   # This will also raise an error
#********************************************
#***********************************************
#Built-in Tuple Methods: count() and index()
# t = (1, 2, 3, 1, 2, 1)
# print(t.count(1)) # Output: 3,number of times 1 appears.
# print(t.index(2)) # Output: 1, index of the first occurrence of 2.
# print(t.index(1, 2)) # Output: 3, index of the first occurrence of 1 starting from index 2.
# # Tuples have very few built-in methods by design (only count and index). 
# # This minimal API emphasizes their role as lightweight, immutable sequences.


#######################Class exercise############################################
# #Create a tuple of mixed data, count an element, find its index.
# [name,grades][name]

students  = (("Sam","Alice", "John", "Ali"),((99,82,92),(78,90,67),(78,90,54),(89,87,78)))
print(students)
sam, grades = students[0][0], students[1][0]
print(sam,grades)


# #Try calling a list-only method (append) and observe the error.
