#Assingment 2
# Count Word Frequency in a Sentence using Dictionary

sentence = input("-> ")
words = sentence.lower().split()
my_dict = {}
for word in words:
    count = words.count(word)
    my_dict[word] = count

for word in sorted(my_dict.keys()):
    print(word, ":", my_dict[word])
    


