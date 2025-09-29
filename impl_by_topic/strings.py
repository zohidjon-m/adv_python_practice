
s1= "Hello"
s2='World'
s3="""this is 
multi-line string"""

s1 = "h"+s1[1:]
print(s1)

print(s2[0])
print(s2[-1])
print(s2[1:3])
print(s2[:3])
print(s2[::-1])


txt = "hello world"
print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.capitalize())

msg = "       hello       "
print(msg)
print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())

sentence = "I love Python"
words = sentence.split()
print(words)
joined = "-".join(words)
print(joined)


text = "I like Java"
print(text)
print(text.replace("Java", "Python"))

print(text.find("Java"))
print(text.find("C++"))



for i, v in enumerate(sentence):
    print(i, v)