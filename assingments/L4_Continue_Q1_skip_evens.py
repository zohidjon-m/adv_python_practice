# Lecture 4 — Continue — Q1: Print 1..10, skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
