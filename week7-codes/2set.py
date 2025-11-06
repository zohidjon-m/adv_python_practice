# # Demonstrating how to create sets 

# fruits = {"apple", "banana", "apple", "cherry"}
# print(fruits)       # what happens to duplicates?
# print("banana" in fruits)



# # --- SET CREATION EXAMPLES ---


# 1 Using a string -> breaks into unique letters
# s1 = set('abracadabra')
# print("s1 =", s1)
# print("type(s1):", type(s1), "\n")

# # 2 Using a list with one word -> treats word as one element
# s2 = set(['abracadabra'])
# print("s2 =", s2)
# print("type(s2):", type(s2), "\n")

# # 3 Using a tuple with one word -> same, one element
# s3 = set(('abracadabra',))
# print("s3 =", s3)
# print("type(s3):", type(s3), "\n")

# # 4 Using a list with one word ('alacazam')
# s4 = set(['alacazam'])
# print("s4 =", s4)
# print("type(s4):", type(s4), "\n")

# # 5 Using a tuple with one word ('alacazam',)
# s5 = set(('alacazam',))
# print("s5 =", s5)
# print("type(s5):", type(s5), "\n")

# # 6 Two elements in a list
# s6 = set(['abracadabra', 'alacazam'])
# print("s6 =", s6)
# print(f"type of s6: {type(s6)}\n")

# # 7 Two elements in a tuple
# s7 = set(('abracadabra', 'alacazam'))
# print("s7 =", s7)
# print(f"type of s7: {type(s7)}\n")

#################Set Operations#####################
# a = set('abracadabra')
# b = set('alacazam')
# print(a)      # unique letters in a
# print(a - b)  # letters in a but not in b
# print(a | b)  # letters in a or b or bothand tuples

# students = {"Alex", "Mina", "John", "Sara"}
# passed = {"Alex", "Sara"}
# failed = students - passed
# print(failed)

#What if we reverse order passed - students?
# print(passed - students)  

#a | b   # union: combine all unique.
# a & b   # intersection:common to both.
# a ^ b   # symmetric difference: in either but not both.

# Group Task:
# “Given:
# A = {"python","java","c"}
# B = {"java","c++","go"}

# Find common languages

# Find all unique languages

# Find languages only in A or only in B.”
##############################################
# 
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.union(B))          # {1, 2, 3, 4, 5, 6}
print(A | B)               # {1, 2, 3, 4, 5, 6}

print(A.intersection(B))   # {3, 4}
print(A & B)               # {3, 4}

print(A.difference(B))     # {1, 2}
print(A - B)               # {1, 2}

print(A.symmetric_difference(B))  # {1, 2, 5, 6}
print(A ^ B)                      # {1, 2, 5, 6}



#############################################
##Set Comprehensions:
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)
##Use set comprehensions for filtering unique items efficiently:
## e.g., extracting unique words, IDs, etc.

# words = ["python","is","fun","and","python","is","fast"]
# unique = {w for w in words if len(w)>2}
# print(unique)
##  How does this differ from using a list comprehension?

A = {"py", "java","c"}
B = {"java", "c++", "go"}

print(f"common languages: {A&B}")
print(f"all unique languages: {A|B}")
print(f"languages only in A and B: {A^B}")
