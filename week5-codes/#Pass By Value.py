# #Pass By Value — Simple Return
# #When you pass arguments to a function, the function gets a copy of the value 

# def addInterest(balance, rate):
#     newBalance = balance * (1 + rate)
#     return newBalance

# def test():
#     amount = 1000
#     rate = 0.05
#     nb = addInterest(amount, rate)
#     print(nb)

# test()
#point: addInterest does not modify amount; 
# it just uses its value to calculate a new one and returns it.
##########Pass By Value — No Return:
#If you don’t return, changes inside the function don’t affect the caller’s variable.
def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    balance = newBalance   # changes local balance only

def test():
    amount = 1000
    rate = 0.05
    #amount = addInterest(amount, rate)
    #How to fix it? Use return:
    print(amount)

test()
#amount stays 1000 because the function changed only its local copy.
#To actually change it, you must return and assign:
#amount = addInterest(amount, rate)
