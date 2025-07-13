# List Ananlysis
# Experiment 02
# Testing pop() time
import timeit
from timeit import Timer

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(pop_zero.timeit(number=1000))


x = list(range(2000000))
print(pop_end.timeit(number=1000))


# While our first test does show that pop(0) is indeed slower than pop(), it does not validate
 # the claim that pop(0) is O(n) while pop() is O(1).
#  Loooking at performance of both over a range of list size
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")
print("pop(0) pop()")
for i in range(1000000,100000001,1000000):
 x = list(range(i))
 pt = pop_end.timeit(number=1000)
 x = list(range(i))
pz = pop_zero.timeit(number=1000)
print("%15.5f, %15.5f" %(pz,pt)) 
