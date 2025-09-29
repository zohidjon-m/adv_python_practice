while True:
    start = int(input("Start: "))
    end = int(input("End: "))
    if start >= 0 and end > start:
        #................
    print("Invalid. End must be > start.")

for i in range(start, end+1):
    if i % 2 == 0:
        #.....................
    print(i)