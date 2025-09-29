# Lecture 4 — Q3: Nested loops (multiplication table 1–5)
for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(f"{i*j:2d}")
    print(" ".join(row))
