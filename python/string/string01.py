spam = "This is Ibrahim Adebanjo's Docuymentation"
print(spam)
# Escape Character "\" (backslash) e.g (\',\",\t,\n,\\)
spam = 'This is Ibrahim Adebanjo\'s Documentation'
print(spam)
print("This is Ibrahim Adebanjo's \n Docuymentation")
print("This is Ibrahim Adebanjo's \t Docuymentation")
# Raw strings (r)
print(r"This is Ibrahim Adebanjo's \t Docuymentation")
# multiple strings with tripple Quotes
print('''Dear Ibrahim,
 Eve's cat has been arrested for catnapping, cat burglary, and extortion.
 Sincerely,
 Bob''')
# Multiline comments
"""This is a test Python program.
 Written by Al Sweigart al@inventwithpython.com
 This program was designed for Python 3, not Python 2.
"""


def spam():
    """
    This is a Multiline comment that explains what this Spam function does 
    """
    print("hello")


spam()
# Strings Indexing and Slicing
spam = "Hello World"
print(spam[0])
print(spam[10])
print(spam[0:10])
print(spam[:5])
print(spam[7:])
# The in and not in Operators with String
print("hello" in spam)
print("World" in spam)
print("cats" not in spam)
print("Dog" in spam)
# USeful string methods
#  upper(), lower(), isupper() and islower()
print(spam.upper())
print(spam.lower())
print(spam.islower())
print(spam.isupper())

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
print(spam.upper().lower().upper())  