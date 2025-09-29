

while True:
    raw = input("Enter an odd integer n (n ≥ 5): ").strip()
    # Only digits allowed (no try/except)
    if not raw.isdigit():
        print("Invalid: please enter digits only.")
        continue

    n = int(raw)
    if n >= 5 and n % 2 == 1:
        break
    else:
        print("Invalid: n must be odd and at least 5. Try again.")
        continue
    


#9x9 rhombus pattern:
print("9x9 rhombus pattern: \n")
for i in range(1, 10):
    for j in range(1, 10):
        if ((i + j == 6) or (j - i == 4) or (i + j == 14) or (i - j == 4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#generalized version for any odd n:
print("generalized version for any odd n:\n")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j == (n // 2 + 2)) or (j - i == n // 2) or (i + j == (n + n // 2 + 1)) or (i - j == n // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()