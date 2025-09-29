# Lecture 3 — Q3: Comparison Operators
x = input("Enter first value: ")
y = input("Enter second value: ")
try:
    xn, yn = float(x), float(y)
    print("Equal?", xn == yn)
except ValueError:
    print("Equal?", x == y)
