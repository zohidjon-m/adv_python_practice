########################################################Example2-1#######
#Odds from 0..n
n = int(input("Enter n:"))
for i in range(n+1):
    if i % 2 == 1:
        print(i, end = " ")

print()
# Point: range excludes the upper bound, so we need n+1
#Notice that 0 gets ignored automatically since it is not odd.
########################################################Example2-2#######
#Odds from 1..n
#We want explicitly skip 0.

n = int(input("Enter n: "))
for i in range(n+1):
    if i == 0:
        pass
    else:
        if i % 2 == 1:
            print(i, end = " ")
print()
# "pass" is a placeholder. It tells Python to “do nothing” but keeps the syntax valid.

#####################################################Example2-3#######
#Extend the idea: skip a range of values (0 and 1) with if i < 2: pass
#Odds from 2..n
n = int(input("Enter n: "))
for i in range(n+1):
    if i < 2:
        pass
    else:
        if i % 2 == 1:
            print(i, end = " ")
print()

#####################################################Example2-4#######
#Odds from 3..n
#Threshold raised to 3
n = int(input("Enter n: "))
for i in range(n+1):
    if i < 3:
        pass
    else:
        if i % 2 == 1:
            print(i, end = " ")
print()

########################################Example2-5#######
#Odds from [start, end]
# Generalize with user-provided start and end values.
# No pass needed anymore.  Logic is more direct.
s = int(input("Enter the starting number: "))
e = int(input("Enter the ending number: "))

for i in range(s, e+1):
    if i % 2 == 1:
        print(i, end = " ")

print()

############################Example2-6################
start = eval(input("Enter a starting number: "))
end = eval(input("Enter an ending number: "))
step = eval(input("Enter the step: "))

for i in range(start, end, step):
    print(i, end = " ")

print()

