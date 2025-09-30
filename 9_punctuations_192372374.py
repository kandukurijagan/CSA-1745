import string
text = input("Enter a string: ")
clean_text = ''.join(char for char in text if char not in string.punctuation)
print("\nOriginal String:")
print(text)
print("\nString after removing punctuations:")
print(clean_text)