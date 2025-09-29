# n = int(input("How many numbers do you have? "))
# sum = 0.0

# for i in range(n):
#         x = float(input("Enter a number >> "))
#         sum = sum + x

# print("\nThe average of the numbers is", sum/n)

########################How we can do it now using a while statement#######
# sum = 0.0
# n = int(input("How many numbers do you have? "))
# count = 0
# while count < n:
#     x = float(input("Enter a number >> "))
#     sum += x   # Note: sum += x is shorthand for sum = sum + x
#     count += 1 # Note: count += 1 is shorthand for count = count + 1
    
# print("The average of the " + str(n) + " numbers you entered is ", sum/n)

#################################################
 #Version that assumes no prior knowledge about the quantity of numbers the user will input
sum = 0.0
count = 0
moreData = "yes"
while moreData == "yes":
    x = float(input("Enter a number >> "))
    sum += x
    count += 1
    moreData = input("Do you have more numbers (yes or no)? ")

print("The average of the " + str(count) + " numbers you entered is ", sum/count)