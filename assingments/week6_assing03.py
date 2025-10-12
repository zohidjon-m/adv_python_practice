# Assignment 3: Demonstrate at least 8 built-in list methods using plain prints only.
# 1) append(x): Add x at the end. Mutates in place.
lst = [1, 2, 3]
b = lst.copy()
lst.append(4)
print("\n=== append ===")
print("Before:", b)
print("lst.append(4)")
print("After: ", lst)

# 2) extend(iterable): Append all items from iterable. Mutates in place.
lst = [1, 2]
b = lst.copy()
lst.extend([3, 4])
print("\n=== extend ===")
print("Before:", b)
print("lst.extend([3, 4])")
print("After: ", lst)

# 3) insert(i, x): Insert x at index i. Mutates in place.
lst = ['a', 'c']
b = lst.copy()
lst.insert(1, 'b')
print("\n=== insert ===")
print("Before:", b)
print("lst.insert(1, 'b')")
print("After: ", lst)

# 4) remove(x): Remove first occurrence of x. Mutates.
lst = ['a', 'b', 'b', 'c']
b = lst.copy()
lst.remove('b')
print("\n=== remove ===")
print("Before:", b)
print("lst.remove('b')")
print("After: ", lst)

# 5) pop([i]): Remove and return item at i (default last). Mutates; returns value.
lst = [10, 20, 30]
b = lst.copy()
r = lst.pop()
print("\n=== pop ===")
print("Before:", b)
print("r = lst.pop()")
print("Returned:", r)
print("After: ", lst)

# 6) index(x[, start[, end]]): Return first index of x. Does not mutate.
lst = ['x', 'y', 'z', 'y']
print("\n=== index ===")
print("List:", lst)
print("lst.index('y') ->", lst.index('y'))
print("After (no mutation):", lst)

# 7) count(x): Return number of occurrences of x. Does not mutate.
print("\n=== count ===")
print("List:", lst)
print("lst.count('y') ->", lst.count('y'))
print("After (no mutation):", lst)

# 8) sort(*, key=None, reverse=False): Sort list in place. Mutates.
lst = [3, 1, 2]
b = lst.copy()
lst.sort()
print("\n=== sort ===")
print("Before:", b)
print("lst.sort()")
print("After: ", lst)

# 9) reverse(): Reverse list in place. Mutates.
lst = [1, 2, 3]
b = lst.copy()
lst.reverse()
print("\n=== reverse ===")
print("Before:", b)
print("lst.reverse()")
print("After: ", lst)

# 10) copy(): Shallow copy of the list. Does not mutate.
lst = [[1], [2]]
c = lst.copy()
print("\n=== copy ===")
print("Original:", lst)
print("Copy:    ", c)
print("Same object? ", lst is c)
