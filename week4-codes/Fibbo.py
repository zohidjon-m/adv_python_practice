n = int(input("Enter a number that is larger than 1 >> "))
if n < 2:
    print("You can only enter a number that is larger than 1!")
else:
    f_i = 0
    f_j = 1
    print(f_i, f_j, end=" ")
for n in range(2, n + 1):   
          f_new = f_i + f_j      
          print(f_new, end=" ")
          f_i = f_j
          f_j = f_new
