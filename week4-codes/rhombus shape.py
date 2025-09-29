for i in range(1, 10):
    for j in range(1, 10):
        if ((i+j== 6) or (j-i==4) or (i+j == 14) or (i-j==4)):
            print("*", end = "")## print star, stay on same line
        else:
            print(" ", end = "")## print space, stay on same line
    print()## move to next line after finishing a row
# ###############################General Version#######
# #row + column == (columns // 2 + 2)  match 6
# #column - row == (columns // 2) 
# #row + column == (columns + math.ceil(rows/2))  match 14
# #row - column == (columns // 2) 
# import math


# while True:
#     rows = int(input("Enter number of rows: "))
#     columns = int(input("Enter number of columns: "))

#     if rows != columns or rows % 2 != 1 or columns % 2 != 1:
#         print("Please enter odd and equal rows and columns")
#     else:
#         break

# rows = abs(rows)
# columns = abs(columns)

# for i in range(1, rows+1):
#     for j in range(1, columns+1):
#         if ((i+j== (columns//2 +2)) or (j-i==(columns//2)) or (i+j == (columns+ math.ceil(rows/2))) or (i-j==(columns//2))):
#             print("*", end = "") ## print star, stay on same line
#         else:
#             print(" ", end = "")## print space, stay on same line
#     print()## move to next line after finishing a row

