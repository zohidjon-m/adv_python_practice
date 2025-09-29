# Lecture 4 — Break — Q2: Keep asking numbers; stop when user enters 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    print("You entered:", n)
