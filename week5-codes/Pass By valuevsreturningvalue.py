#Pass By value
def increment_func(x):
    x = x + 1

val = 1
increment_func(val)
print(val)   # 1 (unchanged)
print(increment_func(val))  # None (no return value)

#Pass By reference
def increment_func(x):
    x = x + 1
    return x

val = 1
val = increment_func(val)
print(val)   # 2 (changed because we used return)
print(increment_func(val))  # 3 (changed because we used return)