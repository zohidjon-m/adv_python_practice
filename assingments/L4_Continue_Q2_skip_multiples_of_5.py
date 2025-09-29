# Lecture 4 — Continue — Q2: Print 1..15, skip multiples of 5
for i in range(1, 16):
    if i % 5 == 0:
        continue
    print(i)
