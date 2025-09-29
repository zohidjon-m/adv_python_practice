
# x = int(input("what is the secret code? enter: "))
# while(x != 43):
#     x = int(input("what is the secret code? enter: "))



x = int(input("what is the secret code? enter: "))
y = 43
while(x != y):
    if x > y:
        print("the number is lower than it")
        x = int(input("what is the secret code? enter: "))
    elif x < y:
        print("the number is higher than it")
        x = int(input("what is the secret code? enter: "))    