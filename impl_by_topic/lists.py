
empty = []                  # empty list
nums = [1, 2, 3, 4, 5]      # integers
mixed = [1, "apple", 3.5]   # mixed types
nested = [[1, 2], [3, 4]]   # list inside a list


print(nums[0])
print(nums[-1])

nums[1]=25

print(nums)

a=[1,3]
b=[4,6]
print(a+b)

print([0]*5)

print(20 in nums)
print(3 in nums)


for i, v, in enumerate(mixed):
    print(i, v)

#list comprehension
squares = [x**2 for x in range(6)]
print(squares)

addition = [x+y for x, y in enumerate(nums)]
print(addition)

#filter
evens = [x+1 for x in range(10) if x%2==0]
print(evens)

#nested comprehension (flatten a list of list)
matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
print(flat)


#slicig
a=[1,2,3]
b=a
b[0]=99
print(a) # [99,2,3] because b just has the reference to the a. it doesn't have the whole separate copy.

#correct way to copy

c = a[:]   #slicing
d= list(a)  # list() function
e = a.copy() #copy method

nums = [1, 2, 3, 4, 5]

copy_by_slice = nums[:]
copy_by_slice[0]=21
print("Slicing:", nums)

copy_by_list_func = list(nums)
print("list() function:", copy_by_list_func)

copy_by_copy_method = nums.copy()
print("copy() method:", copy_by_copy_method)


nums = [10, 20, 30, 40, 50, 60, 70]

# Get first three elements
first_three = nums[:3]
print("First three:", first_three)  # [10, 20, 30]

# Get last three elements
last_three = nums[-3:]
print("Last three:", last_three)    # [50, 60, 70]

# Get every other element
every_other = nums[::2]
print("Every other:", every_other)  # [10, 30, 50, 70]

# Reverse the list
reversed_list = nums[::-1]
print("Reversed:", reversed_list)   # [70, 60, 50, 40, 30, 20, 10]

# Get elements from index 2 to 5 (exclusive)
middle = nums[2:5]
print("Middle slice:", middle)      # [30, 40, 50]