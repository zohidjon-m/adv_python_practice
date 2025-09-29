# Lecture 4 — Q2: While loop (sum of digits)
n = input("Enter a non-negative integer: ").strip()
total= 0
i = 0

while i < len(n):
    if n[i].isdigit():
        total += int(n[i])
    i += 1
print("Sum of digits:", total)
