#The following line will make the math library in Python available for us.
import math

print("This program finds the real solutions to a quadratic.")
print()

a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))

discriminant = b * b - 4 * a * c
if discriminant < 0:
	print("The equation has no real roots!")
else:
    s_root_val = math.sqrt(discriminant)
    root1 = (-b + s_root_val)/(2*a)
    root2 = (-b - s_root_val)/(2*a)
    print("The solutions are: ", root1, root2)
