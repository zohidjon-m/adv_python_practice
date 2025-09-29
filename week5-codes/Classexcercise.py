#Class excercise: Global vs Local Variables:
x = 100

def read_only():
    print(x)  # .........................

def change_it():
    x = x + 1  # ..........................

read_only()
change_it()

#1. Predict what will happen when running this code.
#2. Run it and observe the error message.Add comments to line 5 and line 8 to explain the error.
#3. Fix the error.
#4. Fter solving error add a print statement after the call to show the new value of x.
#5. why x has that value?
