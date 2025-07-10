import math
word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)

sq_list = []
for x in range(1, 11):
    sq_list.append(x * x)
print(sq_list)
# List comprehension
sq_list = [x * x for x in range(1, 11)]
print(sq_list)
# exception handling
a_number = 20
try:
    print(math.sqrt(a_number))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(a_number)))
#  defining a function


def square(n):
    return n ** 2


print(square(3))
print(square(square(3)))


# Square root function
def square_root(n):
  root = n / 2 #initial guess will be 1/2 of n
  for k in range(20):
     root = (1 / 2) * (root + (n / root))
  return root

print(square_root(20))