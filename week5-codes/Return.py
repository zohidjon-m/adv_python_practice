# def square(x):
#     print(x*x)
#     return x * x

# def cube(x):
#         print(x*x*x)
#         return x * x * x

# def power(a, b):
#      print(a**b)
#      return a ** b

# print(square(3))  # 9
# print(cube(3))    # 27
# print(power(2, 3))# 8
# #####################################
# def greet():
#     print("Hello!")

# result = greet()
# print("result is:", result)
# #####################################
# def greet():
#     return "Hello!"

# result = greet()
# print("result is:", result)

# #Key points to remember:
# #In Python, every function call always produces a return value.

# #If you write return something, that “something” is sent back to the caller.

# #If you do not write a return statement, Python automatically returns None.

# # None is a special built-in object that means “no value”.
# # If a function does not have a return statement, it returns None by default.
# # You can use return to send a value back to the caller.
# # Once a return statement is executed, the function exits immediately, 
# # and any code after the return statement will not be executed.
# # If a function has multiple return statements, 
# # only the first one that is executed will determine the return value.
# #Ex1
# def test():
#     print("Before return")
#     return 42
#     print("After return")  #  never runs

# result = test()
# print(result)
# # ######################Ex2
def classify(x):
    if x > 0:
        return "Positive"
    if x < 0:
        return "Negative"
    return "Zero"   # only runs if x == 0

print(classify(5))   # Positive
print(classify(-3))  # Negative
print(classify(0))   # Zero
# Class exercise:
##Write the function from scratch and verify the outputs.
#(Modify it so positive numbers are labeled as “Even Positive” or “Odd Positive”.)