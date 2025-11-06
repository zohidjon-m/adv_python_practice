# divmod()
q, r = divmod(17, 5)
print("divmod(17,5): quotient =", q, ", remainder =", r)

# enumerate()
for i, value in enumerate(["a", "b", "c"]):
    print("Index:", i, "Value:", value)

# tuple()
t = tuple([1, 2, 3])
print("tuple([1,2,3]) returns:", t)

# dict.items()
sample = {"a": 1, "b": 2}
for key, value in sample.items():
    print("Key:", key, "Value:", value)

# os.path.split()
import os
path_info = os.path.split("/home/user/document.txt")
print("os.path.split returns:", path_info)
folder, filename = path_info
print("Folder:", folder)
print("Filename:", filename)
