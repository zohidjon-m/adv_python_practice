# Lecture 3 — Q1: Arithmetic Operators
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", "undefined (division by zero)" if b == 0 else a / b)

