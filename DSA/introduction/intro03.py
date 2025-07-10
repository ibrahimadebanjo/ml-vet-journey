# Euclid's Algorithm
# GCD of two numbers is the largest number that divides both number without eaving a remainder
# using loop
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


print(gcd(20, 10))

class Fraction:
  def __init__(self, top, bottom):
      self.num = top
      self.den = bottom
  def __str__(self):
      return str(self.num) + "/" + str(self.den)
  def show(self):
       print(self.num, "/", self.den)
  def __add__(self, other_fraction):
      new_num = self.num * other_fraction.den + \
      self.den * other_fraction.num
      new_den = self.den * other_fraction.den
      common = gcd(new_num, new_den)
      return Fraction(new_num // common, new_den // common)
  def __eq__(self, other):
      first_num = self.num * other.den
      second_num = other.num * self.den
      return first_num == second_num
x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)

# using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(8,3))
