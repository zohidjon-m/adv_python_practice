# Assignment 1
def swap_case(s):
    out = []
    for ch in s:
        if 'a' <= ch <= 'z':
            out.append(chr(ord(ch) - 32))
        elif 'A' <= ch <= 'Z':
            out.append(chr(ord(ch) + 32))
        else:
            out.append(ch)
    return ''.join(out)

text = input().rstrip("\n")
print(swap_case(text))