#assingment 3
text = input("Enter a string: ")
char_count = {}
for ch in text:
    if ch != " ":
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

for ch in sorted(char_count.keys()):
    print(ch, ":", char_count[ch])
