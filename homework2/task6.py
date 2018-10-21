string = input("Please enter a string:")
list_words = string.split()
# amount of words
length = len(list_words)

# reversing words inside themselves
for i in range(length):
    list_words[i] = list_words[i][::-1]

# concatenation words in one string
string = " ".join([list_words[i] for i in range(length)])

print(string)
