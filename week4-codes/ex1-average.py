n = int(input("How many numbers do you have? "))
sum = 0.0

for i in range(n):
    x = float(input("Enter a number >> "))
    sum = sum + x

print("The average of the numbers is", sum/n)
