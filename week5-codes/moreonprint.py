#more on print function:
# print()      # prints an empty line
# print("Hello")
# print()      # another blank line
# print(3 + 4)                 # 7
# print(3, 4, 3+4)             # 3 4 7
# print("The answer is",3+4)  # The answer is 7
#print can take many expressions separated by commas.
# It inserts a space between them automatically.
#By default, each print() call ends with a newline (\n).
#The end= parameter lets you change what’s printed at the end.
def answer():
    print("The answer is:", end=" ")  # <- no newline, just a space
    print(3 + 4)

answer()
####################
# print("A", end=" ")
# print("B", end=" ")
# print("C")
# # A B C
####################
# for i in range(3):
#     print(i, end=", ")
# # 0, 1, 2,
# print()  # just to end the line
# #The sep= parameter lets you change what’s printed between items.
# print("Hello", "World", sep="-", end="!\n")