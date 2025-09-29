# # Compute the area of a circle three times (for different radii) without using functions
# pi = 3.14159

# r1 = 3
# area1 = pi * r1**2
# print(area1)

# r2 = 5
# area2 = pi * r2**2
# print(area2)

# r3 = 10
# area3 = pi * r3**2
# print(area3)
###############################
################################
# Compute the area of a circle three times (for different radii) using a function
pi = 3.14159


def circle_area(radius):
    return pi * radius**2

print(circle_area(3))
print(circle_area(5))
print(circle_area(10))
