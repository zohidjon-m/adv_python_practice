# # *********************************************************
# # DICTIONARIES IN PYTHON 
# # *********************************************************

# Dictionaries are mutable mappings of keys to values.
# my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print("Original Dictionary:", my_dict)
# print("Type:", type(my_dict), "\n")

# # ------------------------------------------------------------
# # Dictionaries cannot be concatenated (+) or repeated (*)
# # These operations are invalid for dictionaries

# new_dict = my_dict + {'job': 'Engineer'}  #  TypeError
# repeat_dict = my_dict * 2                 #  TypeError
# print("Concatenation and repetition are not supported for dicts.\n")

# # ------------------------------------------------------------
# # Dictionaries can be nested: dict values can be other dicts
# person = {
#     "name": "Alice",
#     "address": {"city": "New York", "zipcode": 10001},
#     "skills": {"Python": "Advanced", "SQL": "Intermediate"}
# }
# print("Nested Dictionary Example:")
# print(person, "\n")

# # ------------------------------------------------------------
# # Dictionaries are mutable and passed by reference
# # Changing one reference affects the other
# a = {"x": 1}
# b = a                # both variables point to the same dictionary
# b["y"] = 2           # modifying b also changes a
# print("Dictionary 'a' after modifying 'b':", a)
# print("Dictionary 'b':", b, "\n")

# # ------------------------------------------------------------
# # Keys must be immutable (strings, numbers, tuples)
# # Immutable keys are allowed:
# valid_dict = {1: "integer key", (2, 3): "tuple key", "str": "string key"}
# print("Valid Keys Example:", valid_dict)
# print("Note: lists cannot be used as keys because they are mutable.\n")

# # ------------------------------------------------------------
# # # Values can be any type (number, list, dict, etc.)
# value_demo = {"num": 42, "list": [1, 2, 3], "dict": {"a": 1}}
# print("Values Can Be Any Type Example:")
# print(value_demo, "\n")

# # ------------------------------------------------------------
# # Keys must be unique within one dictionary
# # Duplicate keys will be overwritten when the dictionary is created
# dup_key = {"x": 1, "y": 2, "x": 99}  # second 'x' overwrites the first
# print("Duplicate Key Overwrite Example:", dup_key, "\n")

# # ------------------------------------------------------------
# # Dictionaries preserve insertion order (since Python 3.7)
# order_demo = {"a": 1, "b": 2, "c": 3}
# print("Insertion Order Is Preserved:", order_demo, "\n")

# # ------------------------------------------------------------
# # Empty dictionary
# empty_dict = {}
# print("Empty Dictionary:", empty_dict, "\n")
# # or using the dict() constructor
# empty_dict2 = dict()
# print("Empty Dictionary Using dict():", empty_dict2, "\n")

# # ------------------------------------------------------------
# Access values by key using indexing [] or the get() method
# my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print("Access value by key using []:", my_dict['name'])
# print("Access value by key using get():", my_dict.get('age'))
# print(my_dict.get(3))
# print("Using get() with a missing key returns:", my_dict.get('job', 'Not Found'), "\n")

# # ------------------------------------------------------------
# # Add or change key:value pairs using indexing []
# my_dict['age'] = 31             # change value
# my_dict['job'] = 'Engineer'     # add new key:value
# print("After Adding/Updating Key:Value Pairs:", my_dict, "\n")

# # ------------------------------------------------------------
# # Delete key:value pairs using del or pop()
# del my_dict['city']             # delete a specific key
# print("After Deleting 'city' Using del:", my_dict)

# removed_value = my_dict.pop('job')  # pop returns the removed value
# print("After Deleting 'job' Using pop():", my_dict)
# print("Removed Value:", removed_value, "\n")

# # ------------------------------------------------------------
# Common dictionary methods demonstration
# d = {'a': 1, 'b': 2, 'c': 3}
# print("keys():", d.keys())        # returns all keys
# print("values():", d.values())    # returns all values
# print("items():", d.items())      # returns key:value pairs

# d_copy = d.copy()                 # make a shallow copy
# print("copy():", d_copy)

# d_copy['d'] = 4

# print(f"The main dic {d}")
# print(f"The copy dic {d_copy}\n")

# d.clear()                         # remove all items
# print("clear():", d)

# fromkeys() creates new dict with given keys and same initial value
# d = dict.fromkeys(['x', 'y', 'z'], 0)
# print("fromkeys():", d)

# # update() adds or modifies multiple items at once
# d.update({'y': 5, 'w': 9})
# print("update():", d)

# # popitem() removes and returns the last inserted key:value pair
# print("popitem() removed:", d.popitem())
# print("After popitem():", d, "\n")

# # ------------------------------------------------------------
# # Iterate through keys, values, and key:value pairs
# student = {'name': 'Alice', 'major': 'CS', 'GPA': 3.8}
# print("Iterating Through Dictionary:")
# for key, value in student.items():
#     print(f"  {key}: {value}")
# print()

# # ------------------------------------------------------------
# # Dictionary comprehension example
# {key_expr: value_expr for item in iterable if condition}
# squares = {x: x**2 for x in range(1, 6)}
# print("Dictionary Comprehension Example (Squares):", squares)

# even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# print("Even Squares Using Comprehension:", even_squares, "\n")

# # ============================================================
# #  IN-CLASS EXERCISE
# # ============================================================

# # Task 1: Create a dictionary of student names and scores.


# # Task 2: Add a new student and update an existing one.

# # Task 3: Delete a student and show remaining keys.


# # Task 4: Use dictionary comprehension to create a new dict that shows pass/fail.
   

                                  

# # ============================================================shallow vs deep copy
# #Shallow Copy: If the dictionary contains nested objects (like lists or other dicts),
# #a shallow copy will copy the outer dictionary, but inner objects are still references to the original.
# #So changes to inner objects in the copy will affect the original.

# original = {'a': 1, 'b': [10, 20]}
# copy_dict = original.copy()

# print("Original:", original)
# print("Copy:", copy_dict)
# copy_dict['b'].append(30)
# print("After modifying copy_dict['b']:", copy_dict)
# print("Original after modifying copy_dict['b']:", original)

#If you want Python to duplicate everything inside — including inner lists or dicts:
#you need a deep copy using the copy module:

# import copy
# original = {'a': 1, 'b': [10, 20]}
# deep_copy = copy.deepcopy(original)

# deep_copy['b'].append(30)
# print("Original:", original)
# print("Deep Copy:", deep_copy)
# #Shallow Copy: Outer container only
# #Deep Copy: Outer + inner containers
# # ============================================================
# Dictionary comprehensions are a concise way to create dictionaries.
# They follow the format: {key_expr: value_expr for item in iterable if condition}
# Example: Create a dictionary of squares for numbers 1-5
# squares = {x: x**2 for x in range(1, 6)}
# print("Squares Dictionary:", squares)
# # Example with condition: Only even squares for numbers 1-10
# even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# print("Even Squares Dictionary:", even_squares)
# ============================================================
#Performance comparison: List vs Set for membership testing    
# import time     
# big_list = list(range(1_000_000))  # List with 1 million integers
# big_set  = set(big_list)
# start = time.time(); 999999 in big_list; print("List time:", time.time()-start)
# start = time.time(); 999999 in big_set;  print("Set time:",  time.time()-start)
#list lookup grows with size (O(n)), set lookup stays about constant (O(1)).
# Sets use hash tables internally, like dictionaries.
# Hash tables use more memory, but are much faster for lookups.
# Use sets when you need fast membership testing and uniqueness.
# Use lists when you need ordered collections, duplicates, or indexing.
# ============================================================



string = "hello my dear how are u dong how are you hello my name is dear bear ?"

words = string.lower().split()
my_dict = {}
for word in words:
    count = words.count(word)
    my_dict[word] = count

sorted_dict = dict(sorted(my_dict.items()))
print("unsorted",my_dict)
print("sorted: ", sorted_dict)



