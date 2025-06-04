spam = "Hello World"
print(spam.join(["This is Ibrahim Adebanjo"]))
print(spam.join(["This is Ibrahim Adebanjo  ",
      "DVM II", "  Ahmadu Bello University", "Zaria"]))
print(spam.split())
print(spam.split("e"))
# A common use of split() is to split a multiline string along the newline characters.
spam = '''Dear Alice,
 How have you been? I am fine.
 There is a container in the fridge
 that is labeled "Milk Experiment".
 Please do not drink it.
 Sincerely,
 Bob'''
print(spam.split('\n'))
