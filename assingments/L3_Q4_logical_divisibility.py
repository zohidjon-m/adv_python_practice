# Lecture 3 — Q4: Logical Operators (divisible by both 2 and 3)
n = int(input("Enter a number: "))
if (n % 2 == 0) and (n % 3 == 0):
    print(n, "is divisible by both 2 and 3")
else:
    print(n, "is NOT divisible by both 2 and 3")
