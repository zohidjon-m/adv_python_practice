# Lecture 4 — Q4: Count vowels in a string
s = input("Enter a string: ")
vowels = set("aeiouAEIOU")
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)
