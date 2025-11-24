

nums = [3,4,6,7,9]

divisible = list(filter(lambda x: x%3==0, nums))
print(divisible)

words = ["cat", "dog", "ant", "bee"]

sorted_words = sorted(words, key = lambda x: x[1])
print(sorted_words)

# Using map, filter, and sorted:
# Step 1: Add 5 to each number
# Step 2: Keep only odd results
# Step 3: Sort in descending order
nums = [2, 7, 4, 8, 3]