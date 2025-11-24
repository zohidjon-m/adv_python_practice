# If you receive a "FileNotFoundError", follow these steps:

# Step 1: Check your current working directory
import os
print("Current working directory:", os.getcwd())

# Step 2: Make sure the text file is in this same folder.
# If not, move the file there or change the path below.
 
# --- Solution 1: Use a relative path (if file is in the same folder)
# file_obj = open("Hello1.txt", "rt")

# --- Solution 2: Use a full path (if file is in another folder)
# Example (Windows): file_obj = open(r"C:\path\to\your\file\Hello1.txt", "rt")
# Example (Mac/Linux): file_obj = open("/Users/username/Desktop/Hello1.txt", "rt")

# --- Solution 3: Change the current working directory in code
# os.chdir(r"path_where_the_file_is_located")
# file_obj = open("Hello1.txt", "rt")

# Now read and print file content
# file_ob1 = open("Hello!.txt", "rb")
# data = file_ob1.read()
# print(data)
# print(type(data))

# f = open("Hello!.txt", "r")
# str1 = f.readline()
# print(str1,end="")
# str2 = f.readline()
# print(str2)
# print(f.readline())

f = open("notes.txt", "w")
f.write("This file contains some information about sales\n")
f.write("Total sales today = QAR100,000\n")
f.write("Sales from PCs = QAR70,000\n")
f.close()


f = open("notes.txt", "r")
str1 = f.readline()
print(str1,end="")
str2 = f.readline()
print(str2)
print(f.readline())

with open("notes.txt","a") as f:
    f.write("This was added safely using with!\n")

print("###########-reading after 'a'-##########")
f = open("notes.txt", "r")
str1 = f.readline()
print(str1,end="")
str2 = f.readline()
print(str2)
print(f.readline(),end="")
print(f.readline())


# f = open("Hello!.txt", "a")
# f.write("This file contains some information about sales\n")
# f.write("Total sales today = QAR100,000\n")
# f.write("Sales from PCs = QAR70,000\n")
# f.close()

# f = open("Hello!.txt", "w")
# print("This file contains some information about sales", file = f)
# print("Total sales today = QAR100,000", file = f)
# print("Sales from PCs = QAR70,000", file = f)
# f.close()


