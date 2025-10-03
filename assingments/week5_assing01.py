# Assignment 1: Real roots of ax^2 + bx + c = 0
import math
def real_quadratic_roots(a, b, c):
    if a == 0:
        # Degenerates to bx + c = 0 (if b != 0) or invalid (if b == 0)
        if b == 0:
            return None
        return (-c / b,)
    disc = b*b - 4*a*c
    if disc < 0:
        return None
    if disc == 0:
        return (-b / (2*a),)
    sqrt_d = math.sqrt(disc)
    return ((-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a))

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

roots = real_quadratic_roots(a, b, c)
if roots is None:
    print("No real solutions (discriminant < 0 or equation invalid).")
elif len(roots) == 1:
    print(f"One real solution: x = {roots[0]}")
else:
    r1, r2 = roots
    print(f"Two real solutions: x1 = {r1}, x2 = {r2}")