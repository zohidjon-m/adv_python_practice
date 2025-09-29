# for i in range(1,10,2):
#     print(i)
    
# for i in range(10,2,-1):
#     print(i)
    

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# for i in range(3):
#     for j in range(2):
#         print(f"({i},{j})", end=" ")
#     print()
    
    
# count = 1
# while count <= 5:
#     print(count)
#     count+=1


for i in range(1,6):
    if i== 3:
        continue
    if i == 5:
        break
    print(i)
    
for i in range(0,6):
    print(" "*i, end="")
    for j in range(1,6-i):
        print(j, end="")
    print()
 

for i in range(0,6):
    print(" "*i, end="")
    print("*"* (6-i))