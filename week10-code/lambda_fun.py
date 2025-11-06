

nums = [3,4,6,7,9]

divisible = list(filter(lambda x: x%3==0, nums))
print(divisible)

words = ["cat", "dog", "ant", "bee"]

sorted_words = sorted(words, key = lambda x: x[1])
print(sorted_words)