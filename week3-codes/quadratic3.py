import math
print("This program finds the real solutions to a quadratic.")
print()
#a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))
discriminant = b * b - 4 * a * c
if discriminant < 0:
        print("The equation has no real roots!")
elif discriminant == 0:
        root = -b/(2*a)
        print("\nThere is a double root at", root)
else:
        s_root_val = math.sqrt(discriminant)
        root1 = (-b + s_root_val)/(2*a)
        root2 = (-b - s_root_val)/(2*a)
        print("The solutions are: ", root1, root2)
