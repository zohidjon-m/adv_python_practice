x1, x2, x3 = eval(input("Please enter three values: "))

if x1 >= x2 and x1 >= x3:
    max = x1
elif x2 > x1 and x2 > x3:
    max = x2
else:
    max = x3

print("The largest value is", max)
