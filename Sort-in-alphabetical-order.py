# change this value for a different result
my_str = str(input("Enter a sentence/words: "))

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
