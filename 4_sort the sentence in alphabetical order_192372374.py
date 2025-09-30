sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort(key=str.lower)
print("The sorted words are:")
for word in words:
    print(word)