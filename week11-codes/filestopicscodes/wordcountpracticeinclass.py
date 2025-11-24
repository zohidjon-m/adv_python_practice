import os
import string

def wordCount(name):
    # TODO: Step 1 – Check if input is a string and if file exists
    if type(name) is str and os.path.exists(name):
        # TODO: Step 2 – Open the file in read mode
        f = open(name)

        # TODO: Step 3 – Initialize counters
        l_c = 0    # line count
        w_c = 0    # word count
        c_c = 0    # character count
        s_c = 0
        p_c = 0

        # TODO: Step 4 – Loop through each line in the file
        for i in f:                     
            l_c = l_c + 1               # Count each line
            s_c = s_c +i.count(" ")
            p_c = p_c + i.count(string.punctuation)
            list_of_words = i.split()   # Split line into words

            # TODO: Count number of words in this line
            w_c = w_c + len(list_of_words)

            # TODO: Count total number of characters (excluding spaces)
            for j in list_of_words:
                c_c = c_c + len(j)      

        # TODO: Step 5 – Create a dictionary with all counts
        dic = {"Line Count": l_c, "Word Count": w_c, "Character Count": c_c, "space count": s_c, "punctuation count": p_c}
        return dic
    else:
        # TODO: Step 6 – Handle missing file case
        print("The file does not exist!")

# TODO: Step 7 – Test your program
# Create a new text file, write several lines, then run:
print(wordCount("file1.txt"))
a = wordCount("file1.txt")
print(a)
# TODO (Extension):
# Try modifying the loop to also count:
# - spaces using: line.count(" ")
# - punctuation using: string.punctuation (import string)
