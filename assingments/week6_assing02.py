# Assignment 2
VOWELS = set('aeiouAEIOU')

def counts(s: str):
    vowels = consonants = blanks = 0
    for ch in s:
        if ch == ' ':
            blanks += 1
        elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            if ch in VOWELS:
                vowels += 1
            else:
                consonants += 1
        # else ignores digits/punctuations
    return vowels, consonants, blanks

text = input()
v, c, b = counts(text)
print(f"Vowels: {v}")
print(f"Consonants: {c}")
print(f"Blanks: {b}")